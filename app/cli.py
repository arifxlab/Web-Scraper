import typer

from app.analytics.statistics import StatisticsService
from app.core.config import settings
from app.core.logger import get_logger
from app.crawler.crawler import WebCrawler
from app.scraper.client import ScraperClient
from app.scraper.robots import RobotsChecker
from app.storage.csv_writer import CSVWriter
from app.storage.json_writer import JSONWriter
from app.validator.validator import DatasetValidator

logger = get_logger(__name__)


app = typer.Typer(
    help="FlyRank Web Scraper CLI",
    no_args_is_help=True,
)


@app.command("crawl")
def crawl_command() -> None:
    """
    Crawl the Books to Scrape website and export the data.
    """

    logger.info("Starting crawl command.")

    robots = RobotsChecker(
        settings.BASE_URL,
        settings.USER_AGENT,
    )

    robots.load()

    with ScraperClient(robots) as client:
        crawler = WebCrawler(client)
        products = crawler.crawl()

    json_output = JSONWriter().write(
        settings.JSON_FILENAME,
        products,
    )

    csv_output = CSVWriter().write(
        settings.CSV_FILENAME,
        products,
    )

    logger.info(
        "Successfully exported %d products.",
        len(products),
    )

    typer.secho(
        "\n✓ Crawl completed successfully!",
        fg=typer.colors.GREEN,
        bold=True,
    )

    typer.echo(f"Products     : {len(products)}")
    typer.echo(f"JSON Output  : {json_output}")
    typer.echo(f"CSV Output   : {csv_output}")


@app.command("stats")
def stats_command() -> None:
    """
    Display statistics about the scraped dataset.
    """

    logger.info("Generating dataset statistics.")

    stats = StatisticsService.from_json(
        f"{settings.OUTPUT_DIRECTORY}/{settings.JSON_FILENAME}"
    ).summary()

    typer.echo("\n" + "=" * 60)

    typer.secho(
        "DATASET STATISTICS",
        fg=typer.colors.CYAN,
        bold=True,
    )

    typer.echo("=" * 60)

    typer.echo(f"Products         : {stats['total_products']}")

    typer.echo(f"Average Price    : £{stats['average_price']:.2f}")

    typer.echo(f"Highest Price    : £{stats['highest_price']:.2f}")

    typer.echo(f"Lowest Price     : £{stats['lowest_price']:.2f}")

    typer.echo(f"Average Rating   : {stats['average_rating']:.2f}")

    typer.echo("\nRating Distribution")
    typer.echo("-" * 30)

    for rating, count in stats["rating_distribution"].items():
        typer.echo(f"{rating} Star : {count}")

    typer.echo("\nAvailability")
    typer.echo("-" * 30)

    for availability, count in stats["availability_distribution"].items():
        typer.echo(f"{availability} : {count}")

    typer.echo("=" * 60)


@app.command("export")
def export_command() -> None:
    """
    Export the existing dataset to all supported formats.
    """

    logger.info("Export command executed.")

    typer.echo("Export command will be implemented in Sprint 17.")


@app.command("validate")
def validate_command() -> None:
    """
    Validate the scraped dataset.
    """

    logger.info("Running dataset validation.")

    report = DatasetValidator.from_json(
        f"{settings.OUTPUT_DIRECTORY}/{settings.JSON_FILENAME}"
    ).validate()

    typer.echo("\n" + "=" * 60)

    typer.secho(
        "DATASET VALIDATION",
        fg=typer.colors.YELLOW,
        bold=True,
    )

    typer.echo("=" * 60)

    typer.echo(f"Records Checked      : {report['records']}")
    typer.echo(f"Duplicate URLs       : {report['duplicate_urls']}")
    typer.echo(f"Missing Titles       : {report['missing_titles']}")
    typer.echo(f"Invalid Prices       : {report['invalid_prices']}")
    typer.echo(f"Invalid Ratings      : {report['invalid_ratings']}")
    typer.echo(f"Invalid Product URLs : {report['invalid_product_urls']}")
    typer.echo(f"Invalid Image URLs   : {report['invalid_image_urls']}")
    typer.echo(f"Missing Availability : {report['missing_availability']}")

    typer.echo()

    if report["passed"]:
        logger.info("Dataset validation passed.")

        typer.secho(
            "Status               : PASSED ✅",
            fg=typer.colors.GREEN,
            bold=True,
        )
    else:
        logger.warning("Dataset validation failed.")

        typer.secho(
            "Status               : FAILED ❌",
            fg=typer.colors.RED,
            bold=True,
        )

    typer.echo("=" * 60)


if __name__ == "__main__":
    app()
