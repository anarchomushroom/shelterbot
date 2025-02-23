import os
import requests
from dotenv import load_dotenv

def check_price():
    # Get CT API Token from .env
    load_dotenv()
    CT_TOKEN = os.getenv("CT_TOKEN")

    # Fetch price info
    url = 'https://api.cardtrader.com/api/v2/marketplace/products?blueprint_id=318079'
    headers = {'Authorization':f'Bearer {CT_TOKEN}'}

    request = requests.get(url, headers=headers)
    json = request.json()
    price = json['318079'][0]['price']['formatted']

    return price