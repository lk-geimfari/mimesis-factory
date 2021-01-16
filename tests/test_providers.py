import factory
import pytest
from mimesis import builtins
from mimesis.enums import Gender
from mimesis.exceptions import UnsupportedField
from pytest_factoryboy import register

from mimesis_factory import MimesisField


class Guest(object):
    def __init__(self, full_name, patronymic):
        self.full_name = full_name
        self.patronymic = patronymic


@register
class FactoryWithNoProviders(factory.Factory):
    class Meta(object):
        model = Guest

    full_name = MimesisField('full_name', gender=Gender.FEMALE)
    patronymic = MimesisField('patronymic')


@register
class FactoryWithProviders(factory.Factory):
    class Meta(object):
        model = Guest

    class Params(object):
        providers = (builtins.RussiaSpecProvider,)

    full_name = MimesisField('full_name', gender=Gender.FEMALE)
    patronymic = MimesisField('patronymic')


def test_factory_with_not_extended_providers(factory_with_no_providers):
    with pytest.raises(UnsupportedField):
        factory_with_no_providers()


def test_factory_with_extended_providers(factory_with_providers):
    guest = factory_with_providers()
    assert isinstance(guest, Guest)
