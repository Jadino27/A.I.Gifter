import csv
import time
import os
import requests
from bs4 import BeautifulSoup
import etsy_api
from config import ETSY_API_KEY
from etsy_api import get_active_listings 

def save_listings_to_csv(listings, filename):
    # Verifica se il file esiste e ha un'intestazione
    file_exists = os.path.isfile(filename) and os.path.getsize(filename) > 0

    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Scrive l'intestazione solo se il file non esiste o è vuoto
        if not file_exists:
            writer.writerow(['listing_id', 'title', 'description', 'tags', 'url', 'price', 'image_url'])

        for listing in listings['results']:
            writer.writerow([
                listing['listing_id'],
                listing['title'],
                listing['description'],
                listing['tags'],
                listing['url'],
                listing['price'],
            ])
            
            print(listing['listing_id'], listing['title'], listing['description'], listing['tags'], listing['url'], listing['price'])

def main():
    total_calls = 5000  # Numero massimo di chiamate all'API per giorno
    limit_per_call = 100  # Numero di risultati per ogni chiamata all'API
    offset = 0  # Inizia da 0

    calls_made = 0

    while calls_made < total_calls:
        listings = get_active_listings(ETSY_API_KEY, offset, limit_per_call)
        if listings:
            save_listings_to_csv(listings, 'active_listings.csv')
            print(f"Saved {len(listings['results'])} listings to CSV.")
            offset += len(listings['results'])  # Incrementa l'offset in base al numero di risultati ottenuti
            calls_made += 1
            print(f"Fetched and saved listings up to offset {offset}")
        else:
            print("No results found.")
            break

        # Aspetta prima di fare la prossima chiamata per rispettare il limite di rate
        time.sleep(1 / 5)  # Aspetta 0.2 secondi tra le chiamate

if __name__ == "__main__":
    main()
