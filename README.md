# Medicine Web Scraping Project

This project is designed to scrape medicine data from various websites using the Scrapy framework. The scraped data is then processed and manipulated using Pandas, saved as a CSV file, and finally stored in a PostgreSQL database.

## Table of Contents

- Installation
- Usage

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/medicine-webscraping.git
    cd medicine-webscraping
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
    - Update example.env to .env then Add PostgreSQL Configurations

## Usage

1. **Run the Scrapy spider:**
    ```bash
    scrapy crawl medicine_spider -o output/medicines.csv
    ```
    or
   check medicine.csv

3. **Process the data using Pandas:**
    core/data_cleaning.ipynb

   

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Resources 

- [WebMD](https://www.webmd.com/drugs/2/alpha/a)



