from mimesis.providers import (
    Address, Business, ClothingSizes,
    Code, Datetime, Development, File,
    Food, Hardware, Internet, Numbers,
    Path, Personal, Science, Structured,
    Transport, Text, UnitSystem, Games,
    Cryptographic,
)


class LocaleDepProvider(Address, Business, Code, Datetime,
                        Personal, Science, Text, Food):
    pass


class CommonProvider(ClothingSizes, Development, File, Hardware,
                     Internet, Numbers, Path, Structured, Transport,
                     UnitSystem, Games, Cryptographic):
    pass


class Provider(LocaleDepProvider, CommonProvider):
    pass
