from .payment_method import PaymentMethod
from .payment_intent import PaymentIntent
from .payment import Payment
from .source import Source
from .web_hook import WebHook

class Paymongo(object):

    def __init__(self, secret_key):
        self.payment_methods = PaymentMethod(secret_key)
        self.payment_intents = PaymentIntent(secret_key)
        self.payments = Payment(secret_key)
        self.sources = Source(secret_key)
        self.webhooks = WebHook(secret_key)
