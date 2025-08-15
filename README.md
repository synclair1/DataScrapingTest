# Instacart Product Scraper

A Python-based scraper for extracting product information from [Instacart](https://www.instacart.com) using **Selenium** and **BeautifulSoup**.  
Supports scraping multiple stores, automatic cookie loading, and output to JSON or CSV.

---

## Features
- Scrapes product **names, prices, and details** from Instacart store pages.
- Works with **multiple stores** or single store mode.
- **Cookie-based login** (avoids constant re-auth).
- **Threaded scraping** for faster multi-store data collection.
- Saves results as **JSON** or **CSV**.

---

## Requirements
- Python 3.8+
- Google Chrome
- ChromeDriver (auto-managed via `webdriver_manager`)
- Instacart account (to access store pages)

---

## Installation

1. **Clone this repository**
```bash
git clone https://github.com/yourusername/instacart-scraper.git
cd instacart-scraper
