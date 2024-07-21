import requests
from bs4 import BeautifulSoup as BS

def fetch_live_market_indices():
    url = "https://www.nseindia.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    }

    session = requests.Session()
    response = session.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BS(response.content, 'html.parser')
        
        indices_container = soup.find_all('div', class_='nav nav-tabs')
        
        # Initialize dictionary to store the values and percentage changes
        indices_values = {
            "NIFTY 50": {"LTP": None, "change": None},
            "NIFTY BANK": {"LTP": None, "change": None},
            "NIFTY FINANCIAL SERVICES": {"LTP": None, "change": None},
            "NIFTY MIDCAP SELECT": {"LTP": None, "change": None}
        }

        # Iterate over the container to find the desired indices
        for container in indices_container:
            # Find all links including those with 'active'
            links = container.find_all('a', class_=['nav-item', 'nav-link', 'nav-link active'])
            for link in links:
                tab_box = link.find('div', class_='tab_box')
                if tab_box:
                    tb_name = tab_box.find('p', class_='tb_name')
                    tb_val = tab_box.find('p', class_='tb_val')
                    tb_per = tab_box.find('p', class_='tb_per')

                    if tb_name and tb_val and tb_per:
                        index_name = tb_name.text.strip()
                        index_value = tb_val.text.strip()
                        index_change = tb_per.text.strip()

                        if index_name in indices_values:
                            indices_values[index_name]["LTP"] = index_value
                            indices_values[index_name]["change"] = index_change

        # Return the values and percentage changes for each index
        return indices_values
    else:
        print(f"Failed to fetch data, status code: {response.status_code}")
        return None

if __name__ == "__main__":
    indices_data = fetch_live_market_indices()
    if indices_data:
        for index, data in indices_data.items():
            print(f"{index}: LTP = {data['LTP']}, Change = {data['change']}")
