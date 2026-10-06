# Webscraper

Een eenvoudige webscraper geschreven in Python.

De gebruiker geeft via de command line een website mee. Het programma haalt de pagina op met `requests` en toont de HTML-code in de terminal.

## Gebruikte libraries

- `requests`
- `click`

## Uitvoeren

Voer het programma uit met `uv`:

```bash
uv run webscraper.py https://www.example.com
```

De URL moet het protocol bevatten, bijvoorbeeld:

```text
https://
```

## Functionaliteit

Momenteel kan het programma:

- Een website als argument ontvangen via `click`
- De website ophalen met `requests`
- De HTML-code van de pagina tonen in de terminal
