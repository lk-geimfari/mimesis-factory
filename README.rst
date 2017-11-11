mimesis_factory
---------------

|Python|

|Logo|

.. |Logo| image:: /media/logo.png
   :target: https://github.com/mimesis-lab/mimesis-factory


Description
-----------
Mimesis integration with `factory_boy`.


Usage
-----

Just look at the example below and you’ll understand how it works:

.. code:: python

    import datetime
    import random

    class Account(object):
        def __init__(self, username, email, name, surname, age):
            self.username = username
            self.email = email
            self.name = name
            self.surname = surname
            self.age = age
            self.password = ''.join(str(random.randint(0, 10)) for _ in range(10))
            self.date_joined = datetime.datetime.today()

        def __str__(self):
            return '{} ({})'.format(self.username, self.email)

Simply use the ``Mimesis`` class from ``mimesis_factory``:

.. code:: python

    import factory
    from mimesis_factory import Mimesis

    from account import Account

    class AccountFactory(factory.Factory):
        class Meta:
            model = Account
        
        username = Mimesis('username', template='l_d')
        name = Mimesis('name', gender='female')
        surname = Mimesis('surname', gender='female')
        age = Mimesis('age', minimum=18, maximum=28)
        email = factory.LazyAttribute(
            lambda o: '%s@example.org' % o.username
        )
        access_token = Mimesis('token', entropy=32)

License
-------

mimesis_factory is released under the MIT License.

.. |Python| image:: https://img.shields.io/badge/python-3.5%2C%203.6-brightgreen.svg
   :target: https://badge.fury.io/py/mimesis