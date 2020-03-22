# -*- coding: utf-8 -*-

import contextlib
from typing import (
    Any,
    ClassVar,
    Dict,
    Iterable,
    Iterator,
    Optional,
    Tuple,
    Type,
)

from factory import declarations
from mimesis import locales
from mimesis.providers.base import BaseProvider
from mimesis.schema import Field, Generic

_CacheKey = Tuple[str, Any]
_Providers = Iterable[Type[BaseProvider]]


class MimesisField(declarations.BaseDeclaration):
    """
    Mimesis integration with FactoryBoy starts here.

    This class provides common interface for FactoryBoy,
    but inside it has Mimesis generators.
    """

    _cached_instances: ClassVar[Dict[_CacheKey, Field]] = {}
    _default_locale: ClassVar[str] = locales.DEFAULT_LOCALE

    def __init__(
        self, field: str, locale: Optional[str] = None, **kwargs,
    ) -> None:
        """
        Creates a field instance.

        The created field is lazy. It also receives build time parameters.
        These parameters are not applied yet.

        Args:
            field: name to be passed to ``Field`` from ``Mimesis``.
            locale: locale to use. This parameter has the highest priority.
            kwargs: optional parameters that would be passed to ``Field``.

        """
        super().__init__()
        self.locale = locale
        self.kwargs = kwargs
        self.field = field

    def evaluate(
        self, instance, step, extra: Optional[Dict[str, Any]],
    ) -> Generic:
        """Evaluates the lazy field."""
        kwargs: Dict[str, Any] = {}
        kwargs.update(self.kwargs)
        kwargs.update(extra or {})

        providers = step.builder.factory_meta.declarations.get('providers')
        mimesis = self._get_cached_instance(
            locale=self.locale,
            providers=providers,
        )
        return mimesis(self.field, **kwargs)

    @classmethod
    @contextlib.contextmanager
    def override_locale(cls, locale: str) -> Iterator[None]:
        """
        Overrides unspecified locales.

        Remember, that implicit locales would not be overridden.
        """
        old_locale = cls._default_locale
        cls._default_locale = locale  # noqa: WPS601
        yield
        cls._default_locale = old_locale  # noqa: WPS601

    @classmethod
    def _get_cached_instance(
        cls,
        locale: Optional[str] = None,
        providers: Optional[_Providers] = None,
    ) -> Field:
        if locale is None:
            locale = cls._default_locale

        key = (locale, providers)
        if key not in cls._cached_instances:
            cls._cached_instances[key] = Field(locale, providers=providers)

        return cls._cached_instances[key]
