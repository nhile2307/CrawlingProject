# Scrapy Newegg GPU Scraper

This Scrapy project scrapes data from the Newegg GPUs category and stores it in a CSV file. 
Website: [https://www.newegg.com/GPUs-Video-Graphics-Cards/SubCategory/ID-48?Tid=7709]([url](https://www.newegg.com/GPUs-Video-Graphics-Cards/SubCategory/ID-48?Tid=7709))

## Setup
1. Clone this repository.
2. Install Scrapy by running: `pip install scrapy`.

## Usage
Run the spider using the command: `scrapy crawl newegg_spider`.

## File Structure
- `spiders/`: Contains spider files.
- `items.py`: Defines Scrapy items.
- `pipelines.py`: Handles data processing and export.

## CSV Output
The scraped data is exported to `output.csv`.

## Contribution
Feel free to contribute or report issues.
