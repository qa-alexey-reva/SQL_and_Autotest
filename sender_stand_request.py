import requests
import configuration
import data

def create_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER, json=body)

def get_order_track():
    answer = create_new_order(data.order_body)
    return answer.json()["track"]

def get_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_NUMBER + str(track))
