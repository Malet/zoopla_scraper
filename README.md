# Zoopla data scraper

## Prerequisites
* Python 3.5.0

## Getting started
1. run `pip install -r requirements.txt` to install the dependencies.
2. `python scrape.py` to start scraping data.
3. run `bash postgreSQL.sh` to install and config the postgreSQL server

## Mission
The mission for this scraper is to overcome the restrictions of Zoopla's
official API. The rate-limiting of 100 requests per hour is too restrictive
to get you anywhere if you want to run any interesting statistics.
