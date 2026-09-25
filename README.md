# Amazon Scraper

A web scraper built with Python and Selenium to collect product information from Amazon Brazil.

> **Learning project:** This project was created to practice browser automation, HTML element location, explicit waits, and data extraction using Selenium.

## 📌 Features

* Automatically accesses Amazon Brazil.
* Waits for page elements to load.
* Extracts product names using XPath.
* Extracts product prices.
* Displays product information in the terminal.
* Uses `WebDriverWait` and Expected Conditions.

## 🛠️ Technologies

* Python 3
* Selenium
* Google Chrome
* ChromeDriver

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/d4vidlinux/Amazon-Scraper.git
cd Amazon-Scraper
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install selenium
```

## ▶️ Usage

Run the scraper:

```bash
python3 app.py
```

The browser will open automatically and the script will access Amazon Brazil, locate the products, and display the extracted information in the terminal.

Example output:

```text
Echo Dot (Geração… R$459,00
Amazon Fire TV St… R$349,90
Kindle 16 GB (Ger… R$799,00
Smart TV TCL 32… R$1.049,00
Kit 12 Pares Meias… R$31,99
Chinelo Havaianas… R$43,99
Tenis Infantil De A… R$57,99
Babuche Infantil A… R$69,90
```

## ⚙️ How It Works

The scraper uses Selenium to control the browser and extract information from the page.

Basic workflow:

```text
Start WebDriver
      ↓
Open Amazon Brazil
      ↓
Wait for page elements
      ↓
Locate product names
      ↓
Locate product prices
      ↓
Pair names and prices
      ↓
Display results
```

Product names and prices are paired using Python's `zip()` function:

```python
for name, price in zip(products["name"], products["price"]):
    print(name.text, price.text)
```

## ⚠️ Limitations

This project depends on Amazon's current HTML structure and XPath selectors. If the website structure changes, the scraper may stop working correctly.

The current implementation is intentionally simple and does not yet include:

* Pagination
* Complete error handling
* JSON/CSV export
* Logging
* Automated tests
* Modular architecture

These features may be added as the project evolves.

## 🎯 Purpose

The main purpose of this project is to practice:

* Web scraping
* Selenium
* XPath
* `WebDriverWait`
* Expected Conditions
* Python data structures
* Browser automation
* Data extraction and organization

## 📚 Status

**Learning project — in development.**

The project will be improved as new Python and software development concepts are learned.

## 👤 Author

**d4vidlinux**
