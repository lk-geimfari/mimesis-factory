# -*- coding: utf-8 -*-

import string

import factory
from pytest_factoryboy import register

from mimesis_factory import MimesisField


class Person(object):
    def __init__(self, full_name_en, full_name_ru):
        self.full_name_en = full_name_en
        self.full_name_ru = full_name_ru


@register
class PersonFactory(factory.Factory):
    class Meta:
        model = Person

    full_name_en = MimesisField('full_name')
    full_name_ru = MimesisField('full_name', locale='ru')


def test_data_with_different_locales(person):
    for letter in person.full_name_en.replace(' ', ''):
        assert letter in string.ascii_letters

    for russian_letter in person.full_name_ru.replace(' ', ''):
        assert russian_letter not in string.ascii_letters


def test_data_with_override_locale(person_factory):
    with MimesisField.override_locale('ru'):
        person = person_factory()

    for letter in person.full_name_en.replace(' ', ''):
        # Default locale will be changed to overridden:
        assert letter not in string.ascii_letters

    for russian_letter in person.full_name_ru.replace(' ', ''):
        assert russian_letter not in string.ascii_letters


def test_data_with_override_defined_locale(person_factory):
    with MimesisField.override_locale('en'):
        person = person_factory()

    for letter in person.full_name_en.replace(' ', ''):
        assert letter in string.ascii_letters

    for russian_letter in person.full_name_ru.replace(' ', ''):
        # Keyword locale has a priority over override:
        # Some surnames in some locales contains «'» in surname.
        assert russian_letter not in string.ascii_letters + "'"
