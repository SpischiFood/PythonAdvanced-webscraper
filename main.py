import requests
import click
from bs4 import BeautifulSoup
import re
from collections import Counter
from spellchecker import SpellChecker
from urllib.parse import urljoin

MAX_DIEPTE = 1


def scrape_website(website, teller = 0, bezocht = [], diepte = 0):

    if website in bezocht:
        return

    bezocht.add(website)

    spell = SpellChecker(language="nl")
    res = requests.get(website)
    soup = BeautifulSoup(res.text, 'html.parser')
    text = soup.get_text()
    wordlist = re.findall(r"\b[a-zA-z]+\b", text)
    bekende_woorden = spell.known(wordlist)
    correcte_woorden = []

    for woord in wordlist:
        if woord.lower() in bekende_woorden:
            correcte_woorden.append(woord.lower())

    teller.update(correcte_woorden)
    ##Niet verder zoeken
    if diepte >= MAX_DIEPTE:
        return

    ## Links zoeken

    links = soup.find_all(href=True)
    hrefs = [link["href"] for link in links]

    absolute_links = []

    for href in hrefs:
        absolute_url = urljoin(website, href)

        if absolute_url.startswith(("https://", "http://")):
            absolute_links.append(absolute_url)

    for link in absolute_links:
        scrape_website(link, teller, bezocht, diepte + 1)

@click.command()
@click.argument("website")
def scraper(website):
    teller = Counter()
    bezocht = set()

    scrape_website(website, teller, bezocht)
    print(teller)

        

if __name__== "__main__":
    scraper()

