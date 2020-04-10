import requests
import json

payment_intent_url = 'https://api.paymongo.com/v1/payment_intents'
payment_method_url = 'https://api.paymongo.com/v1/payment_methods'
payment_source_url = 'https://api.paymongo.com/v1/sources'
payment_url = 'https://api.paymongo.com/v1/payments'
hook_url = 'https://api.paymongo.com/v1/webhooks'
headers = {'content-type': 'application/json'}


class Paymongo(object):
    def __init__(self, secret_key):
        self.payment_intent_id = None
        self.payment_method_id = None
        self.secret_key = secret_key

    def create_payment_method(self, payload):
        response = requests.post(payment_method_url, data=json.dumps(payload), headers=headers,
                                 auth=(self.secret_key, ''))
        self.payment_method_id = response.json()['data']['id']
        return response.json()

    def get_payment_method(self, key):
        response = requests.get(payment_method_url + '/' + key, auth=(self.secret_key, ''))
        return response.json()

    def create_payment_intent(self, payload):
        response = requests.post(payment_intent_url, data=json.dumps(payload), headers=headers,
                                 auth=(self.secret_key, ''))
        self.payment_intent_id = response.json()['data']['id']
        return response.json()

    def get_payment_intent(self, key):
        response = requests.get(payment_intent_url + '/' + key, auth=(self.secret_key, ''))
        return response.json()

    def attach_payment_intent(self):
        if not self.payment_method_id:
            return {"error": "No payment method id. Create payment method using create_payment_method"}

        if not self.payment_intent_id:
            return {"error": "No payment intent id. Create payment method using create_payment_intent"}

        payment_attached_url = 'https://api.paymongo.com/v1/payment_intents/' + self.payment_intent_id + '/attach'
        payload = {
            "data": {
                "attributes": {"client_key": "card",
                               "payment_method": self.payment_method_id
                               }
            }
        }
        response = requests.post(payment_attached_url, data=json.dumps(payload), headers=headers,
                                 auth=(self.secret_key, ''))
        return response.json()

    def create_source(self, payload):
        response = requests.post(payment_source_url, data=json.dumps(payload), headers=headers,
                                 auth=(self.secret_key, ''))
        json_res = response.json()
        return {"id": json_res['data']['id'],
                "checkout_url": json_res['data']['attributes']['redirect']['checkout_url']}

    def create_payment(self, payload):
        response = requests.post(payment_url, data=json.dumps(payload), headers=headers,
                                 auth=(self.secret_key, ''))
        return response.json()

    def list_payments(self):
        response = requests.get(payment_url, auth=(self.secret_key, ''))
        return response.json()

    def get_payment(self, key):
        response = requests.get(payment_url + '/' + key, auth=(self.secret_key, ''))
        return response.json()

    def create_hook(self, payload):
        response = requests.post(hook_url, data=json.dumps(payload), headers=headers,
                                 auth=(self.secret_key, ''))
        return response.json()

    def list_hooks(self):
        response = requests.get(hook_url, auth=(self.secret_key, ''))
        return response.json()

    def get_hook(self, key):
        response = requests.get(hook_url + '/' + key, auth=(self.secret_key, ''))
        return response.json()

    def disable_hook(self, key):
        response = requests.post(hook_url + '/' + key + '/disable', headers=headers, auth=(self.secret_key, ''))
        return response.json()

    def enable_hook(self, key):
        response = requests.post(hook_url + '/' + key + '/enable', headers=headers, auth=(self.secret_key, ''))
        return response.json()
