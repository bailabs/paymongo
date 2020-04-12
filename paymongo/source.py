import requests
import json
from .urls import payment_source_url
from .constants import headers


class Source(object):

    def __init__(self, secret_key):
        self.secret_key = secret_key

    def create(self, payload):
        response = requests.post(payment_source_url, data=json.dumps(payload), headers=headers,
                                 auth=(self.secret_key, ''))
        json_res = response.json()
        return {"id": json_res['data']['id'],
                "checkout_url": json_res['data']['attributes']['redirect']['checkout_url']}