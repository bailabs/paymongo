import time
from paymongo import Paymongo

secret_key = 'sk_test_.....'
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

# start credit/debit card
print("=================================")
print(paymongo.create_payment_intent(payment_intent_payload))
print("=================================")
print(paymongo.create_payment_method(payment_method_payload))
print("=================================")
print(paymongo.attach_payment_intent())
# end credit/debit card

# start e-wallets
# payment_source_payload = {
#     "data": {
#         "attributes": {"type": "gcash",
#                        "amount": 10000,
#                        "currency": "PHP",
#                        "redirect": {
#                            "success": "https://wela.online",
#                            "failed": "https://bai.ph"
#                        }
#                        }
#     }
# }
#
# response_source = paymongo.create_source(payment_source_payload)
# payment_source_id = response_source['id']
# print(response_source['checkout_url'])
# time.sleep(15)
#
# payment_payload = {
#     "data": {
#         "attributes": {"description": "test2",
#                        "statement_descriptor": "test3",
#                        "amount": 10000,
#                        "currency": "PHP",
#                        "source": {
#                            "id": payment_source_id,
#                            "type": "source"
#                        }
#                        }
#     }
# }
# print(paymongo.create_payment(payment_payload))
# end e-wallets

