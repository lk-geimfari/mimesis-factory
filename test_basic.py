import factory
from pytest_factoryboy import register

from account import Account


@register
class AccountFactory(factory.Factory):
    class Meta:
        model = Account

    username = factory.Sequence(lambda n: 'john%s' % n)
    email = factory.LazyAttribute(lambda o: '%s@example.org' % o.username)


def test_account_exists(account):
    assert account.username == 'john0'
    assert account.email == 'john0@example.org'

