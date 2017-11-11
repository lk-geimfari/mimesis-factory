import factory
from pytest_factoryboy import register

from account import Account
from mimesis_factory import Mimesis


@register
class AccountFactory(factory.Factory):
    class Meta:
        model = Account

    username = Mimesis(
        provider='personal',
        field='full_name',
        locale='ru',
        gender='female'
    )
    email = factory.LazyAttribute(
        lambda o: '%s@example.org' % o.username
    )


def test_account_exists(account):
    print('\n')
    print(account.username)
    assert account.username != 'john0'
    assert account.email != 'john0@example.org'
