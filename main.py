import requests
import click
from bs4 import BeautifulSoup
import re

@click.command()
@click.argument("website")

def scraper(website):
    res = requests.get(website)
    soup = BeautifulSoup(res.text, 'html.parser')
    text = soup.get_text()
    print(re.findall(r"\b[a-zA-Z]+\b", text))

if __name__== "__main__":
    scraper()

