import requests
import json
from .urls import payment_method_url
from .constants import headers


class PaymentMethod(object):
    def __init__(self, secret_key):
        self.secret_key = secret_key

    def create(self, payload):
        response = requests.post(payment_method_url, data=json.dumps(payload), headers=headers,
                                 auth=(self.secret_key, ''))
        return response.json()['data']

    def retrieve(self, key):
        response = requests.get(payment_method_url + '/' + key, auth=(self.secret_key, ''))
        return response.json()['data']
