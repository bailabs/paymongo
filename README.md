# Paymongo Python Library

The Paymongo Python library provides convenient access to the Paymongo API from
applications written in the Python language. It includes a pre-defined set of
classes for API resources that initialize themselves dynamically from API
responses which makes it compatible with a wide range of versions of the Paymongo
API.

- [Installation](#installation)
- [Usage](#usage)
- [Payment Methods](#payment-methods)
  - [Create](#payment-methods---create)
  - [Retrieve](#payment-methods---retrieve)
- [Payment Intents](#payment-intents)
  - [Create](#payment-intents---create)
  - [Retrieve](#payment-intents---retrieve)
- [Sources](#sources)
  - [Create](#sources-create)
- [Payments](#payments)
  - [Create](#payments-create)
  - [List](#payments-list)
  - [Retrieve](#payments-retrieve)
- [Tokens (Deprecated)](#tokens)
- [Webhooks](#webhooks)
  - [Create](#webhooks-create)
  - [List](#webhooks-list)
  - [Retrieve](#webhooks-retrieve)
  - [Toggle (Enable or Disable)](#webhooks-toggle)
- [Test Cards](#test-cards)
- [FAQs](#faqs)

### INSTALLATION

You don't need this source code unless you want to modify the package. If you just
want to use the package, just run:

```sh
pip install --upgrade paymongo
```

Install from source with:

```sh
python setup.py install
```

### USAGE

```python
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
```

### PAYMENT METHODS

[Official Docs](https://developers.paymongo.com/reference#the-payment-method-object)

A `PaymentMethod` resource describes which payment method was used to fulfill a payment. It is used with a `PaymentIntent` to collect payments.

> `paymongo.payment_methods`

#### Payment Methods - Create

```javascript
/**
 * These are the required properties
 * @param {Object} data The payload.
 * @param {Object} data.attributes Payload attributes.
 * @param {string} data.attributes.type The type of payment method. The possible value is card for now.
 * @param {string} data.attributes.details.card_number Credit/Debit Card number of the PaymentMethod.
 * @param {number} data.attributes.details.exp_month Expiry month of the Credit/Debit Card.
 * @param {number} data.attributes.details.exp_year Expiry year of the Credit/Debit Card.
 * @param {string} data.attributes.details.cvc CVC of the Credit/Debit Card.
 */
result = paymongo.payment_methods.create(data);
```

*Payload*

```js
payment_method_payload = {
    "data": {
        "attributes": {"type": "card",
                       "details": {"card_number": "4343434343434345", "exp_month": 10, "exp_year": 22, "cvc": "123"}
                       }
    }
}
```

#### Payment Methods - Retrieve

```python
/**
 * @param {string} id The PaymentMethod id
 */
result = paymongo.payment_method.retrieve(id);
```

### PAYMENT INTENTS

[Official Docs](https://developers.paymongo.com/reference#the-payment-intent-object)

A `PaymentIntent` resource is used to track and handle different states of the payment until it succeeds.

> `paymongo.payment_intents`

#### Payment Intents - Create

```javascript
/**
 * These are the required properties
 * @param {Object} data The payload.
 * @param {Object} data.attributes Payload attributes.
 * @param {number} data.attributes.amount Amount to be collected by the PaymentIntent.
 * @param {string[]} data.attributes.payment_method_allowed The list of payment method types that the PaymentIntent is allowed to use. Possible value is card for now.
 * @param {string} data.attributes.currency Three-letter ISO currency code, in uppercase. PHP is the only supported currency as of the moment.
 */
result = paymongo.payment_intents.create(data);
```

*Payload*

```javascript
payment_intent_payload = {
    "data": {
        "attributes": {"amount": 10000, "payment_method_allowed": ["card"], "description": "test1",
                       "statement_descriptor": "test2",
                       "payment_method_options": {"card": {"request_three_d_secure": "automatic"}}, "currency": "PHP"}
    }
}
```

#### Payment Intents - Retrieve

```javascript
/**
 * @param {string} id token id
 */
result = paymongo.payment_intents.retrieve(id);
```

**Attach to PaymentIntent**

```javascript
/**
 * These are the required properties
 * @param {string} id PaymentIntent id.
 * @param {Object} data The payload.
 * @param {Object} data.attributes Payload attributes.
 * @param {string} data.attributes.payment_method Id of PaymentMethod to attach to the PaymentIntent.
 */
result = paymongo.payment_intents.attach(id, data);
```

*Payload*

```javascript
payload = {
    "data": {
        "attributes": {"client_key": "card",
                       "payment_method": method_id
                       }
    }
}
```

### SOURCES

[Official Docs](https://developers.paymongo.com/reference#the-sources-object)

A Source is a resource to generate your customer's payment instrument. This is normally used to generate check out URLs for e-wallet payments. To learn more about e-wallet integrations, you can visit [GCash](https://developers.paymongo.com/docs/accepting-gcash-payments) or [GrabPay](https://developers.paymongo.com/docs/accepting-grabpay-payments) integration.

> `paymongo.sources`

#### Sources - Create

```javascript
/**
 * These are the required properties
 * @param {Object} data payload
 * @param {Object} data.attributes payload attributes
 * @param {string} data.attributes.type The type of source. Possible values are gcash and grab_pay.
 * @param {number} data.attributes.amount amount int32
 * @param {string} data.attributes.currency Three-letter ISO currency code, in uppercase. PHP is the only supported currency as of the moment.
 * @param {Object} data.attributes.redirect
 * @param {string} data.attributes.redirect.success success url
 * @param {string} data.attributes.redirect.failed error url
 */
const result = await paymongo.sources.create(data);
```

*Payload*

```javascript
{
  data: {
    attributes: {
      type: 'gcash',
      amount: 20000, // PHP200,
      currency: 'PHP',
      redirect: {
        success: 'https://yoururl.com/success',
        failed: 'https://yoururl.com/failed'
      }
    }
  }
}
```

### PAYMENTS

[Official Docs](https://developers.paymongo.com/reference#payment-source)

A `Payment` resource is an attempt by your customer to send you money in exchange for your product. This is a reference to an amount that you are expecting to receive if a payment resource with paid status becomes a part of a payout. If the payment status is `failed`, you can determine the reason for failure.

> `paymongo.payments`

#### Payments - Create

```javascript
/**
 * These are the required properties
 * @param {Object} data payload
 * @param {Object} data.attributes payload attributes
 * @param {number} data.attributes.amount amount int32
 * @param {number} data.attributes.currency Three-letter ISO currency code, in uppercase. PHP is the only supported currency as of the moment.
 * @param {Object} data.attributes.source the source object from checkout
 * @param {string} data.attributes.source.id id of a Source resource
 * @param {string} data.attributes.source.type type of a Source resource. Possible value is 'source'.
 */
result = paymongo.payments.create(data);
```

*Payload*

```javascript
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
```

#### Payments - List

```javascript
result = paymongo.payments.list();
```

*Result*

```javascript
{
  data: [] // array of payments
}
```

#### Payments - Retrieve

```javascript
/**
 * @param {string} id payment id
 */
result = paymongo.payments.retrieve();
```

### WEBHOOKS

[Official Docs](https://developers.paymongo.com/reference#enable-a-webhook)

A `Webhook` resource primarily refers to a certain URL where we send events that are happening from your account. You can check our [GCash](https://developers.paymongo.com/docs/accepting-gcash-payments) and [GrabPay](https://developers.paymongo.com/docs/accepting-grabpay-payments) integrations to find out some good use cases for webhooks.

> `paymongo.webhooks`

#### Webhooks - Create

```javascript
/**
 * These are the required properties
 * @param {Object} data payload
 * @param {Object} data.attributes payload attributes
 * @param {string} data.attributes.url The destination URL of the events that happened from your account. Please make sure that the URL is publicly accessible in order for you to receive the event.
 * @param {string[]} data.attributes.events The list of events to be sent to this webhook. Possible value in the meantime is source.chargeable.
 */
const result = await paymongo.webhooks.create(data);
```

*Payload*

```javascript
{
  data: {
    attributes: {
      url: 'https://yourwebsite.com/webook-listener', // Developer's note: this is unique in paymongo. You can't create multiple webhooks with same url.
      events: ['source.chargeable'] // The only event supported for now is 'source.chargeable'.
    }
  }
}
```

#### Webhooks - List

```javascript
result = paymongo.webhooks.list();
```

*Result*

```javascript
{
  data: [] // Array of webhooks
}
```

#### Webhooks - Retrieve

```javascript
/**
 * @param {string} id Webhook id
 */
result = paymongo.webhooks.retrieve(id);
```

#### Webhooks - Toggle

Enable or disable a webhook.

```javascript
/**
 * @param {string} id webhook id
 * @param {string} action 'enable' or 'disable'
 */
result = paymongo.webhooks.toggle(id, action);
```

### TEST CARDS

| Card Number | Brand | CVC | Expiration Date |
| ----------- | ----- | --- | --------------- |
| 4343434343434345 | Visa | Any 3 digits | Any future date |
| 4571736000000075 | Visa (debit) | Any 3 digits | Any future date |
| 5555444444444457 | Mastercard | Any 3 digits | Any future date |
| 2221000000000918 | Mastercard (2-series) | Any 3 digits | Any future date |
| 5455590000000009 | Mastercard (debit) | Any 3 digits | Any future date |
| 5339080000000003 | Mastercard (prepaid) | Any 3 digits | Any future date |

More cards [here](https://developers.paymongo.com/docs/testing), including [3D Secure Test Cards](https://developers.paymongo.com/docs/testing#section-3-d-secure-test-card-numbers).

### FAQs

- How to make payment using gcash or grabpay?
  - GCash guide - https://developers.paymongo.com/docs/accepting-gcash-payments
  - GrabPay guide - https://developers.paymongo.com/docs/accepting-grabpay-payments

Made with :heart: by Chris Ian Fiel / Wela School System
