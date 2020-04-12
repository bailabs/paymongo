import requests
import json
from .urls import payment_url
from .constants import headers


class Payment(object):

    def __init__(self, secret_key):
        self.secret_key = secret_key

    def create(self, payload):
        response = requests.post(payment_url, data=json.dumps(payload), headers=headers,
                                 auth=(self.secret_key, ''))
        return response.json()

    def retrieve(self, key):
        response = requests.get(payment_url + '/' + key, auth=(self.secret_key, ''))
        return response.json()

    def list(self):
        response = requests.get(payment_url, auth=(self.secret_key, ''))
        return response.json()
