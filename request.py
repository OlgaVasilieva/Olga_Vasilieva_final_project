import data
import config
import requests

def post_new_order(order_body):
    return requests.post(config.URL + config.create_order_path, json=order_body)
response = post_new_order(data.order_body)

def get_new_order_track():
    order_response = post_new_order(data.order_body)
    return order_response.json()["track_id"]

def get_new_order():
    return requests.get(config.create_order_path + order_response.json())
response = get_new_order

