import requests
import click

@click.command()
@click.argument("website")

def scraper(website):
    res = requests.get(website)

    print(res.text)

if __name__== "__main__":
    scraper()

