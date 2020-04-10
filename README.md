# Paynongo Python Library

The Paynongo Python library provides convenient access to the Paynongo API from
applications written in the Python language. It includes a pre-defined set of
classes for API resources that initialize themselves dynamically from API
responses which makes it compatible with a wide range of versions of the Stripe
API.

## Documentation

See the [Paymongo API Docs]https://developers.paymongo.com/docs).

## Installation

You don't need this source code unless you want to modify the package. If you just
want to use the package, just run:

```sh
pip install --upgrade paymongo
```

Install from source with:

```sh
python setup.py install
```

### Requirements

-   Python 2.7+ or Python 3.4+ (PyPy supported)

## Usage

The library needs to be configured with your account's secret key which is
available in your [Paymongo Dashboard][api-keys]. 

```python
from paymongo import Paymongo

paymongo = Paymongo('sk_test_.....')


# list payments
paymongo.list_payments()

# retrieve single Customer
paymongo.get_payment("pay_3j46sohyuPa1siEA5LHoPzJM")
```
