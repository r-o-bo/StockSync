import requests
import os
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

def check_rate_lim():
    try:
        res = requests.get(url=my_url,headers=needed_headers)
        res.raise_for_status() 
        stat_code = res.status_code
    
        daily_limits = res.headers.get('x-ratelimit-requests-limit')
        daily_remaining = res.headers.get('x-ratelimit-requests-remaining')
        calls_per_min_allowed = res.headers.get('X-RateLimit-Limit')
        calls_per_min_remaining = res.headers.get('X-RateLimit-Remaining')


        rate_limits = {
            'daily_limit': daily_limits,
            'daily_remaining': daily_remaining,
            'minute_limit': calls_per_min_allowed,
            'minute_remaining': calls_per_min_remaining
        }

        print(stat_code) # 200 if OK
        print(rate_limits)

        return rate_limits
    
    except requests.exceptions.HTTPError as err:
        print("HTTP error occurred:", err)
        print("Response text:", res.text)

        return None

# check_rate_lim() call to check rate limits

# API call for json data
res2 = requests.get(url=my_url,headers=needed_headers)

if res2.status_code == 200:
    data = res2.json()

    print(json.dumps(data,indent=2))

else:
    print("failed to fetch data from API")

    




    
