import requests
from bs4 import BeautifulSoup
import re

base_url = "http://quotes.toscrape.com/page/"

file_path = "./quotes.txt"

with open(file_path, "a", encoding="utf-8") as file:
    for page_num in range(1, 11):  # Scrape quotes from page 1 to 10
        url = base_url + str(page_num)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        
        quotes = soup.find_all("div", class_="quote")
        
        for quote in quotes:
            quote_text = quote.get_text().strip()
            quote_text = re.sub(r"\(about\)", "", quote_text)
            quote_text = re.sub(r"Tags:", "", quote_text)  
            quote_text = re.sub(r"", "", quote_text)  
            file.write(quote_text)
            file.write("\n")
