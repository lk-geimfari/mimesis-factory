import factory
from pytest_factoryboy import register

from account import Account
from mimesis_factory import Mimesis


@register
class AccountFactory(factory.Factory):
    class Meta:
        model = Account

    username = Mimesis('mime_type', type_t='image')
    email = factory.LazyAttribute(
        lambda o: '%s@example.org' % o.username
    )


def test_account_exists(account):
    assert account.username != 'john0'
    assert account.email != 'john0@example.org'
