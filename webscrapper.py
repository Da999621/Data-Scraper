import requests
from bs4 import BeautifulSoup
import csv

# Target URL (you can change this to a real news/product site)
URL = "https://quotes.toscrape.com/"  # Example site 

# Step 1: Send HTTP request to the website
response = requests.get(URL)

# Step 2: Check response status
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Step 3: Extract data (e.g., quote text and author)
    quotes_data = []
    quotes = soup.find_all('div', class_='quote')
    for quote in quotes:
        text = quote.find('span', class_='text').get_text(strip=True)
        author = quote.find('small', class_='author').get_text(strip=True)
        quotes_data.append([text, author])

    # Step 4: Save data to CSV file
    with open('scraped_quotes.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Quote', 'Author'])  # Header row
        writer.writerows(quotes_data)

    print("Data scraped and saved to 'scraped_quotes.csv'.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
