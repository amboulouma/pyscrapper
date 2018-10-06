import requests
from bs4 import BeautifulSoup

page = requests.get(
    "https://en.wikipedia.org/wiki/Web_scraping")

soup = BeautifulSoup(page.content, 'html.parser')
print([p.get_text() for p in soup.find_all("p")])
