# terminal-google
Google via shell.

This script runs a web-driver (phantomjs) to execute google's javascript and pull search query results.

Granted it might not be the fanciest of ways to get the data (there is an API, after all) it serves its purpose quite well.

Run via: ./googleScraper.py 'search_query' --links

(--links is optional but it includes full links, which may be pretty long for certain queries).

# Requirements:
- phantomjs
- BeautifulSoup
- splinter
- python3
