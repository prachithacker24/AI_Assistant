import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# Send a GET request to the website
url = 'https://prachithacker24.github.io/Clothing_Website/cart.html'
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')
print(soup)
# Extract data from the HTML content
data = []
for i in soup.find_all('tr'):
    row = []
    for j in i.find_all('td'):
        row.append(j.text.strip())
    if row:
        data.append(row)

# Convert the extracted data into a DataFrame
df = pd.DataFrame(data[1:], columns=data[0])

# Drop any rows with missing values
df = df.dropna(axis=0, how='any')

# Get the column names from the DataFrame
column_names = df.columns

# Convert data types of columns
for col in column_names:
    if col == 'Price':
        df[col] = pd.to_numeric(df[col])
    elif col == 'Quantity':
        df[col] = pd.to_numeric(df[col])

# Calculate total cost for each item
df['Total Cost'] = df['Price'] * df['Quantity']

# Perform some data analysis
analysis_data = df[['Item', 'Total Cost']]

# Create a bar chart using matplotlib
plt.bar(analysis_data['Item'], analysis_data['Total Cost'])
plt.xlabel('Items')
plt.ylabel('Total Cost')
plt.title('Data Analysis')
plt.show()

# Save the DataFrame to an Excel file
df.to_excel('output.xlsx', index=False)

# Save the DataFrame to a PDF file
df.to_pdf('output.pdf', index=False)