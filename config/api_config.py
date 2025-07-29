import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

base_url = "https://yahoo-finance127.p.rapidapi.com"

needed_headers = {
    'x-rapidapi-key': API_KEY,
    'x-rapidapi-host': "yahoo-finance127.p.rapidapi.com"
}

def check_rate_lim():
    my_url = f"{base_url}/price"
    res = requests.get(url=my_url,headers=needed_headers,params={"symbol": "eth-usd"})

    
