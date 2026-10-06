import requests
import click
from bs4 import BeautifulSoup
import re
from collections import Counter
from spellchecker import SpellChecker

@click.command()
@click.argument("website")

def scraper(website):
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

    teller = Counter(correcte_woorden)
    print(teller)

    ## Links zoeken
    print("\nLinks: ")

    links = soup.find_all(href=True)
    hrefs = [link["href"] for link in links]
    print(hrefs)

if __name__== "__main__":
    scraper()

