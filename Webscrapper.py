import requests
from bs4 import BeautifulSoup
import csv
import time
from selenium import webdriver


# Initialize an empty list to store the scraped data
results = []
other_results = []

# Initialize a webdriver
driver = webdriver.Chrome()

# Send a GET request to the website and get its content
driver.get('https://www.myntra.com/shop/men')
time.sleep(5)
content = driver.page_source

# Use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(content, 'html.parser')

# Extract the data from the HTML content
for i in soup.find_all(attrs={'class': 'product-card'}):
    name = i.find('h4')
    price = i.find(attrs={'class': 'price-wrapper'})
    results.append(name.text)
    other_results.append(price.text)

# Write the scraped data to a CSV file
with open('names.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["Names", "Prices"])
    for i in range(len(results)):
        writer.writerow([results[i], other_results[i]])

# Close the webdriver
driver.quit()