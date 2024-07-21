# Fetch NSE Indices
 A Python script to fetch and parse live market index data from the NSE India website. It retrieves the Last Traded Price (LTP) and percentage change for key indices and stores the results in a dictionary.


### Features:

- Fetches data from NSE India
- Extracts LTP and percentage change for selected indices
- Handles HTTP request errors

### Requirements:

- Python 3.x
- requests
- beautifulsoup4

### How to use

<code>
from fetchNSEindices import fetch_live_market_indices

# Fetch the live market indices
indices = fetch_live_market_indices()

# Check if the data was fetched successfully
if indices:
    for index, data in indices.items():
        print(f"{index}: LTP = {data['LTP']}, Change = {data['change']}")
else:
    print("Failed to retrieve market indices.")

</code>
