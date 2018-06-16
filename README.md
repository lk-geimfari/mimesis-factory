## mimesis_factory

[![Build Status](https://travis-ci.org/mimesis-lab/mimesis-factory.svg?branch=master)](https://travis-ci.org/mimesis-lab/mimesis-factory)
[![Coverage](https://coveralls.io/repos/github/mimesis-lab/mimesis-factory/badge.svg?branch=master)](https://coveralls.io/github/mimesis-lab/mimesis-factory?branch=master)
[![Python](https://img.shields.io/badge/python-3.5%2C%203.6-brightgreen.svg)](https://badge.fury.io/py/mimesis)
[![PyPI version](https://badge.fury.io/py/mimesis-factory.svg)](https://badge.fury.io/py/mimesis-factory)

<a href="https://github.com/mimesis-lab/mimesis-factory">
    <p align="center">
        <img src="/media/logo.png">
    </p>
</a>


## Description

Mimesis integration for [`factory_boy`](https://github.com/FactoryBoy/factory_boy).

## Installation

```python
➜  pip install mimesis_factory
```


## Usage

Look at the example below and you’ll understand how it works:

```python
class Account(object):
    def __init__(self, username, email, name, surname, age):
        self.username = username
        self.email = email
        self.name = name
        self.surname = surname
        self.age = age
```

Now, use the `MimesisField` class from `mimesis_factory`
to define how fake data is generated:

```python
import factory
from mimesis_factory import MimesisField

from account import Account

class AccountFactory(factory.Factory):
    class Meta:
        model = Account
        
    username = MimesisField('username', template='l_d')
    name = MimesisField('name', gender='female')
    surname = MimesisField('surname', gender='female')
    age = MimesisField('age', minimum=18, maximum=90)
    email = factory.LazyAttribute(
        lambda o: '%s@example.org' % o.username
    )
    access_token = MimesisField('token', entropy=32)
```


## pytest

We also recommend to use [`pytest-factoryboy`](https://github.com/pytest-dev/pytest-factoryboy).
This way it will be possible to integrate your factories into `pytest` fixtures.


## License

mimesis_factory is released under the MIT License.
