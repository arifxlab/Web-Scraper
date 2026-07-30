# 📚 FlyRank Web Scraper

A production-inspired Python web scraping application that collects product data from **Books to Scrape**, validates the dataset, generates analytics, and exports structured results in JSON and CSV formats.

This project was developed as part of the FlyRank Backend AI Engineering Internship to demonstrate clean architecture, testing, automation, and maintainable backend development practices.

---

## ✨ Features

- Crawl multiple pages automatically
- Respect `robots.txt`
- Configurable request delay
- Custom User-Agent support
- HTML parsing with BeautifulSoup
- Product extraction
- Data cleaning and normalization
- Dataset validation
- Analytics generation
- Export to CSV
- Export to JSON
- Structured logging
- Command Line Interface (Typer)
- Unit testing with Pytest
- Code formatting with Black
- Linting with Ruff
- GitHub Actions CI

---

## 📂 Project Structure

```
app/
├── analytics/
├── core/
├── crawler/
├── extractor/
├── models/
├── parser/
├── scraper/
├── storage/
├── utils/
└── validator/

tests/

data/

logs/
```

---

## 🛠 Tech Stack

- Python 3.11+
- Requests
- BeautifulSoup4
- Pydantic
- Typer
- Pytest
- Ruff
- Black

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/arifxlab/FlyRank-Web-Scraper.git
cd FlyRank-Web-Scraper
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it.

Windows

```powershell
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

---

## ⚙ Configuration

Create a `.env` file:

```env
BASE_URL=https://books.toscrape.com/

USER_AGENT=FlyRank-Web-Scraper/1.0

REQUEST_DELAY=1.5

TIMEOUT=30
```

---

## ▶ Running the scraper

Run:

```bash
python -m app.main
```

or

```bash
python app/main.py
```

---

## 📊 Output

The scraper exports:

- JSON dataset
- CSV dataset
- Dataset validation report
- Statistics summary
- Console logs

Example fields:

- Title
- Price
- Availability
- Rating
- Product URL
- Image URL

---

## 📈 Analytics

The analytics module generates:

- Total products
- Average price
- Highest price
- Lowest price
- Average rating
- Rating distribution
- Availability distribution

---

## ✅ Validation

The validator checks:

- Duplicate URLs
- Missing titles
- Missing availability
- Invalid ratings
- Invalid prices

---

## 🧪 Testing

Run the complete test suite:

```bash
pytest
```

Run linting:

```bash
ruff check .
```

Run formatting check:

```bash
black --check .
```

---

## 🏗 Architecture

The project follows a modular architecture with clearly separated responsibilities.

- Scraper
- Parser
- Extractor
- Cleaner
- Validator
- Analytics
- Storage
- CLI

Each module has a single responsibility, making the project easier to test, maintain, and extend.

---

## 📌 Future Improvements

- Async scraping
- SQLite/PostgreSQL storage
- Retry and backoff strategies
- Pagination improvements
- Docker support
- API integration
- Scheduling support
- Dashboard for analytics

---

## 📚 Educational Purpose

This project uses the **Books to Scrape** website, which is designed specifically for practicing web scraping techniques. It is intended for educational and learning purposes.

---

## 👨‍💻 Author

**Arif Khan**

Backend Software Engineer | AI Engineering Enthusiast

GitHub: https://github.com/arifxlab

---

## 📄 License

This project is licensed under the MIT License.