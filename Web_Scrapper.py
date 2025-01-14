import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        # Fetch the webpage
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for HTTP errors

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract titles and links
        print("Titles and Links from the webpage:\n")
        for tag in soup.find_all('a', href=True):
            title = tag.text.strip() if tag.text else "No Title"
            link = tag['href']
            print(f"Title: {title}, Link: {link}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")

# Test with a sample website
scrape_website("https://en.wikipedia.org/wiki/Main_Page")
scrape_website("https://www.fandom.com/")
scrape_website("https://www.citizendium.org/")