import logging

import typer

from app.core.config import settings
from app.crawler.crawler import WebCrawler
from app.scraper.client import ScraperClient
from app.scraper.robots import RobotsChecker
from app.storage.json_writer import JSONWriter


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(message)s",
)


app = typer.Typer(
    help="FlyRank Web Scraper CLI",
    no_args_is_help=True,
)


@app.command("crawl")
def crawl_command() -> None:
    """Crawl the Books to Scrape website."""

    robots = RobotsChecker(
        settings.BASE_URL,
        settings.USER_AGENT,
    )

    robots.load()

    with ScraperClient(robots) as client:
        crawler = WebCrawler(client)
        products = crawler.crawl()

    output = JSONWriter().write(
        "products.json",
        products,
    )

    typer.secho(
        "\n✓ Crawl completed successfully!",
        fg=typer.colors.GREEN,
        bold=True,
    )

    typer.echo(f"Products : {len(products)}")
    typer.echo(f"Output   : {output}")


@app.command("stats")
def stats_command() -> None:
    """Show crawl statistics."""
    typer.echo("Stats command coming in Sprint 11.")


@app.command("export")
def export_command() -> None:
    """Export data."""
    typer.echo("Export command coming in Sprint 11.")


@app.command("validate")
def validate_command() -> None:
    """Validate dataset."""
    typer.echo("Validate command coming in Sprint 11.")


if __name__ == "__main__":
    app()