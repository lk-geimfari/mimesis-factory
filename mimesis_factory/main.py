from factory import declarations
from mimesis import Generic


class Mimesis(declarations.OrderedDeclaration):
    def __init__(self, provider, field, locale=None, seed=None, **kwargs):
        self.locale = locale
        self.mimesis = Generic(self.locale, seed=seed)
        self.provider = provider
        self.method_kwargs = kwargs
        self.field = field

    def generate(self, extra_kwargs):
        print(extra_kwargs)
        provider = getattr(self.mimesis, self.provider)
        field = getattr(provider, self.field)
        return field(**self.method_kwargs)

    def evaluate(self, sequence, obj, create, extra=None, containers=()):
        print(sequence, obj, create, extra, containers)
        return self.generate(extra or {})
