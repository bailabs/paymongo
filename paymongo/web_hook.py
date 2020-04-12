import requests
import json
from .urls import hook_url
from .constants import headers


class WebHook(object):

    def __init__(self, secret_key):
        self.secret_key = secret_key

    def create(self, payload):
        response = requests.post(hook_url, data=json.dumps(payload), headers=headers,
                                 auth=(self.secret_key, ''))
        return response.json()['data']

    def list(self):
        response = requests.get(hook_url, auth=(self.secret_key, ''))
        return response.json()['data']

    def retrieve(self, key):
        response = requests.get(hook_url + '/' + key, auth=(self.secret_key, ''))
        return response.json()['data']

    def toggle(self, key, action):
        response = requests.post(hook_url + '/' + key + action, headers=headers, auth=(self.secret_key, ''))
        return response.json()['data']
