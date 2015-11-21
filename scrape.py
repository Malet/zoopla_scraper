from bs4 import BeautifulSoup
from IPython import embed
from urllib.parse import urlencode, urlunparse
import json
import os
import requests
import sys

def parse_price(str):
    price = (str
    .strip()
    .replace(',', '')
    .replace(u'\xa3', ''))

    try:
        return int(price)
    except:
        return None

def parse_listing(listing):
    price_node = listing.find('a', class_='text-price')
    try:
        price = list(price_node.children)[2]
    except:
        price = price_node.get_text()

    return {
        'listing_id' : int(listing.attrs['data-listing-id']),
        'price'      : parse_price(price)
    }

def parse_listings(listings):
    return map(parse_listing, listings)

params = {
    'q': 'london',
    'new_homes': 'include',
    'results_sort': 'newest_listings',
    'search_source': 'for-sale',
    'include_retirement_homes': 'true',
    'include_shared_ownership': 'true',
    'page_size': 5,
    'page_number': 1
}

url = urlunparse([
    'http',
    'www.zoopla.co.uk',
    'for-sale/property/london/',
    '',
    urlencode(params),
    ''
])

soup = BeautifulSoup(requests.get(url).content, 'html.parser')

listings = parse_listings(
    soup.find_all('li', attrs={'data-listing-id': True})
)

list(map(print,listings))
