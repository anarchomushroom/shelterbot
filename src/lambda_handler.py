# Import modules
from check_price import check_price
from send_post import send_post

def lambda_handler(event, context):
    send_post()

lambda_handler('event', 'context')