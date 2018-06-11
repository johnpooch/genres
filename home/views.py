from django.shortcuts import render
import bs4 as bs
from urllib.request import urlopen

# Set a URL that we'll try to grab some HTML from.
url = "https://en.wikipedia.org/wiki/Web_scraping"

# Open the URL and read the HTML content into a string variable
html_page = urlopen(url)
html_text = html_page.read()

# Print html_test string
print(html_text)