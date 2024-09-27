# Medicine Web Scraping Project

This project is designed to scrape medicine data from various websites using the [Scrapy framework](https://scrapy.org/). The scraped data is then processed and manipulated using [Pandas](https://pandas.pydata.org/), saved as a CSV file, and finally stored in a PostgreSQL database.

## Table of Contents

- Installation
- Usage
- Resource

## Installation

1. **Clone the repository:**
    ```bash
    https://github.com/Ashmil114/Madicine-Scraping.git
    cd Madicine-Scraping
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up PostgreSQL:**
    - Ensure PostgreSQL is installed and running.
    - Create a database and user for the project.
    - Update [example.env](https://github.com/Ashmil114/Madicine-Scraping/blob/main/example.env) to .env then Add PostgreSQL Configurations

## Usage

1. **Run the Scrapy spider:**
    ```bash
    scrapy crawl medicinespider -o output/medicines.csv
    ```
    or
   Check [medicine.csv](https://github.com/Ashmil114/Madicine-Scraping/blob/main/medicine.csv)

3. **Process the data using Pandas:**
    Check [core/data_cleaning.ipynb](https://github.com/Ashmil114/Madicine-Scraping/blob/main/core/data_cleaning.ipynb)

## Resources 

- [WebMD](https://www.webmd.com/drugs/2/alpha/a)



