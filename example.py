import time
from paymongo import Paymongo

secret_key = 'sk_test_ja5gekYdtRBVochpcK433ejp'
payment_intent_payload = {
    "data": {
        "attributes": {"amount": 10000, "payment_method_allowed": ["card"], "description": "test1",
                       "statement_descriptor": "test2",
                       "payment_method_options": {"card": {"request_three_d_secure": "automatic"}}, "currency": "PHP"}
    }
}

payment_method_payload = {
    "data": {
        "attributes": {"type": "card",
                       "details": {"card_number": "4343434343434345", "exp_month": 10, "exp_year": 22, "cvc": "123"}
                       }
    }
}

paymongo = Paymongo(secret_key)

### start credit/debit card

# intent_data = paymongo.payment_intents.create(payment_intent_payload)
# intent_id = intent_data['id']
# method_data = paymongo.payment_methods.create(payment_method_payload)
# method_id = method_data['id']
# payload = {
#     "data": {
#         "attributes": {"client_key": "card",
#                        "payment_method": method_id
#                        }
#     }
# }
# print(paymongo.payment_intents.attach(intent_id, payload))

### end credit/debit card

# start e-wallets
payment_source_payload = {
    "data": {
        "attributes": {"type": "gcash",
                       "amount": 10000,
                       "currency": "PHP",
                       "redirect": {
                           "success": "https://wela.online",
                           "failed": "https://bai.ph"
                       }
                       }
    }
}

response_source = paymongo.sources.create(payment_source_payload)
payment_source_id = response_source['id']
print(response_source['checkout_url'])
time.sleep(15)

payment_payload = {
    "data": {
        "attributes": {"description": "test2",
                       "statement_descriptor": "test3",
                       "amount": 10000,
                       "currency": "PHP",
                       "source": {
                           "id": payment_source_id,
                           "type": "source"
                       }
                       }
    }
}
print(paymongo.payments.create(payment_payload))
# end e-wallets

