# Import modules
import os
import requests
from dotenv import load_dotenv
from atproto import Client
from datetime import date

# Load .env file and get API login
load_dotenv()

BSKY_USER = os.getenv("BSKY_USER")
BSKY_PASS = os.getenv("BSKY_PASS")
CT_TOKEN = os.getenv("CT_TOKEN")

# Get information from CardTrader API
url = 'https://api.cardtrader.com/api/v2/marketplace/products?blueprint_id=318079'
headers = {'Authorization':f'Bearer {CT_TOKEN}'}

request = requests.get(url, headers=headers)
json = request.json()
price = json['318079'][0]['price']['formatted']

# Connect to Bluseky

client = Client()
client.login(BSKY_USER, BSKY_PASS)

today_day = date.today().strftime("%A")
today_date = date.today().strftime("%B %d, %Y")

post_text = f"It is {today_day}, {today_date}, and the cheapest Shelter of the Storm on Card Trader costs {price}"

client.send_post(text=post_text)