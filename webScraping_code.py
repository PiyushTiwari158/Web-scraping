import pandas as pd
import requests
from bs4 import BeautifulSoup


# Load the excel file into a Pandas DataFrame
df = pd.read_excel(r'C:\Users\Adarsh\Downloads\Web Scraping Assignment.xlsx', sheet_name='Web Scraping Assignment')
# Create a new column for the college address
df['Address'] = ''

# Loop through the rows in the DataFrame
for i, row in df.iterrows():
    try:
        website = row['Website']
    except KeyError:
        # If the 'Website' column does not exist, move on to the next iteration
        continue

    # Make a request to the website
    response = requests.get(website)
    html = response.text

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Look for the address information on the page
    address = soup.find('div', {'class': 'address'})

    # If the address information is found, add it to the DataFrame
    if address:
        df.at[i, 'Address'] = address.text.strip()
    else:
        df.at[i, 'Address'] = ''

# Write the updated DataFrame to the excel file
df.to_excel('colleges_with_address.xlsx', index=False)
