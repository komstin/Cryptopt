import pandas as pd
import requests
import re
from bs4 import BeautifulSoup

# Create date range for historical snapshots
Date = pd.date_range(start='20130428', end='20171210', freq='7D').strftime('%Y%m%d')

# Retrieve market cap value in dollars
market_cap = []

for date in Date:

    # Retrieve historical snapshot data from date
    page = requests.get('https://coinmarketcap.com/historical/'+date)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Extract marketcap value from span
    market_cap.append(int(re.sub(r',|\$', '', soup.find('span', {'id' : 'total-marketcap'}).text.strip())))

# Create data frame of data
df = pd.DataFrame({'Total Market Cap':market_cap}, index=Date)

# Write data to file
df.to_csv('total_market_cap.csv')
