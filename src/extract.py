import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

base_url = "https://yahoo-finance127.p.rapidapi.com"

needed_headers = {
    'x-rapidapi-key': API_KEY,
    'x-rapidapi-host': "yahoo-finance127.p.rapidapi.com"
}
symbol = "eth-usd"
my_url = f"{base_url}/price/{symbol}"

def my_crypto_summary():
    try:
        res = requests.get(url=my_url,headers=needed_headers)
        res.raise_for_status()
        data = res.json()

        summary = {
            # symbol is symbol
            "symbol": data.get("symbol"),
            # name is name
            "name": data.get("shortName", data.get("longName")),
            # price is price
            "price": data.get("regularMarketPrice", {}).get("raw"),
            # gets raw price change
            "price_change": data.get("regularMarketChange", {}).get("raw"),
            # gets the formatted percent str
            "percent_change": data.get("regularMarketChangePercent", {}).get("fmt"),
            # gets the trading volume
            "volume": data.get("regularMarketVolume", {}).get("raw"),
            # market capitialization value
            "market_cap": data.get("marketCap", {}).get("raw"),
            # highest value in last year
            "week_high": data.get("fiftyTwoWeekHigh", {}).get("raw"),
            # lowest value in last year
            "week_low": data.get("fiftyTwoWeekLow", {}).get("raw"),
            # gets teh coins logo
            "logo": data.get("logoUrl"),
            # most recent market update
            "last_updated": data.get("regularMarketTime", {}).get("fmt")
        }

        return summary
    
    except requests.exceptions.HTTPError as http_error_message:
        print(f"[HTTP ERROR]: {http_error_message}")
    
    except requests.exceptions.ConnectionError as connection_error_message:
        print(f"[CONNECTION ERROR]: {connection_error_message}")
    
    except requests.exceptions.Timeout as timeout_error_message:
        print(f"[TIMEOUT ERROR]: {timeout_error_message}")
    
    except requests.exceptions.RequestException as e:
        print(f"[UNKNOWN ERROR]: {e}")

    finally:
        print("Finished attempting api request")

    return None

print(my_crypto_summary())
