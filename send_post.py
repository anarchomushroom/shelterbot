import os
from check_price import check_price
from dotenv import load_dotenv
from atproto import Client
from datetime import date

def send_post():
    # Connect to bsky
    load_dotenv()

    BSKY_USER = os.getenv("BSKY_USER")
    BSKY_PASS = os.getenv("BSKY_PASS")

    client = Client()
    client.login(BSKY_USER, BSKY_PASS)

    # Fetch price data
    price = check_price()

    # Compose post
    today_day = date.today().strftime("%A")
    today_date = date.today().strftime("%B %d, %Y")

    post_text = f"It is {today_day}, {today_date}, and the cheapest Shelter of the Storm on Card Trader costs {price}"

    return client.send_post(text=post_text)