# -*- coding: utf-8 -*-

import contextlib

from factory import declarations
from mimesis import locales
from mimesis.schema import Field


class MimesisField(declarations.BaseDeclaration):
    """
    Mimesis integration with FactoryBoy starts here.

    This class provides common interface for FactoryBoy,
    but inside it has Mimesis generators.

    That's how it works:
    1. We have
    """

    _CACHED_INSTANCES = {}
    _DEFAULT_LOCALE = locales.DEFAULT_LOCALE

    def __init__(self, field, locale=None, **kwargs):
        """
        Creates a field instance.

        The created field is lazy.
        It also receives build time parameters.
        This parameters are not applied yet.

        Args:
            field: field name to be passed to `Field` from `Mimesis`.
            locale: locale to use. This parameter has the highest priority
                over other locale parameters.
            kwargs: optional parameters that would be passed to `Field`.

        """
        super().__init__()

        self.locale = locale
        self.kwargs = kwargs
        self.field = field

    def evaluate(self, instance, step, extra):
        """Evaluates the lazy field."""
        if extra is None:
            extra = {}

        kwargs = {}
        kwargs.update(self.kwargs)
        kwargs.update(extra)

        providers = step.builder.factory_meta.declarations.get('providers')
        mimesis = self._get_cached_instance(locale=self.locale,
                                            providers=providers)
        return mimesis(self.field, **kwargs)

    @classmethod
    @contextlib.contextmanager
    def override_locale(cls, locale):
        """
        Overrides unspecified locales.

        Remember, that implicit locales would not be overridden.
        """
        old_locale = cls._DEFAULT_LOCALE
        cls._DEFAULT_LOCALE = locale
        try:
            yield
        finally:
            cls._DEFAULT_LOCALE = old_locale

    @classmethod
    def _get_cached_instance(cls, locale=None, providers=None):
        if locale is None:
            locale = cls._DEFAULT_LOCALE

        key = (locale, providers)
        if key not in cls._CACHED_INSTANCES:
            cls._CACHED_INSTANCES[key] = Field(locale, providers=providers)

        return cls._CACHED_INSTANCES[key]
