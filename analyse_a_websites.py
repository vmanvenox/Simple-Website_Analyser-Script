# Import the required libraries
from bs4 import BeautifulSoup
import pandas as pd
import requests

# Use requests to download the website's HTML content
response = requests.get('https://www.example.com/prices.html')
html = response.text

# Use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(html, 'html.parser')

# Find all elements with the 'price' class
prices = soup.find_all(class_='price')

# Extract the text from each element and convert it to a float
prices = [float(price.text) for price in prices]

# Create a pandas DataFrame from the list of prices
df = pd.DataFrame(prices, columns=['Price'])

# Calculate some basic statistics about the prices
mean_price = df['Price'].mean()
max_price = df['Price'].max()
min_price = df['Price'].min()

# Print the results
print(f'Mean price: ${mean_price:.2f}')
print(f'Max price: ${max_price:.2f}')
print(f'Min price: ${min_price:.2f}')

# made by KingTreemox aka Treemox