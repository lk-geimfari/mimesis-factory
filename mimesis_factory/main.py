from factory import declarations
from mimesis_factory.provider import Provider


class Mimesis(declarations.OrderedDeclaration):
    def __init__(self, field, locale=None, seed=None, **kwargs):
        self.locale = locale
        self.seed = seed
        self.mimesis = Provider(self.locale, self.seed)
        self.kwargs = kwargs
        self.field = field

    def generate(self, extra_kwargs):
        print(extra_kwargs)
        field = getattr(self.mimesis, self.field)
        return field(**self.kwargs)

    def evaluate(self, sequence, obj, create, extra=None, containers=()):
        print(sequence, obj, create, extra, containers)
        return self.generate(extra or {})
