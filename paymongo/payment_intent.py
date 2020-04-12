import requests
import json
from .urls import payment_intent_url
from .constants import headers


class PaymentIntent(object):
    def __init__(self, secret_key):
        self.secret_key = secret_key

    def create(self, payload):
        response = requests.post(payment_intent_url, data=json.dumps(payload), headers=headers,
                                 auth=(self.secret_key, ''))
        return response.json()['data']

    def retrieve(self, key):
        response = requests.get(payment_intent_url + '/' + key, auth=(self.secret_key, ''))
        return response.json()['data']

    def attach(self, key, payload):
        payment_attached_url = 'https://api.paymongo.com/v1/payment_intents/' + key + '/attach'
        response = requests.post(payment_attached_url, data=json.dumps(payload), headers=headers,
                                 auth=(self.secret_key, ''))
        return response.json()['data']
