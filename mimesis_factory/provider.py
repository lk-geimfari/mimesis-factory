from mimesis.providers import (
    Address, Business, ClothingSize,
    Code, Datetime, Development, File,
    Food, Hardware, Internet, Numbers,
    Path, Person, Science, Structure,
    Transport, Text, UnitSystem, Games,
    Cryptographic,
)


class LocaleDepProvider(Address, Business, Code, Datetime,
                        Person, Science, Text, Food):
    pass


class CommonProvider(ClothingSize, Development, File, Hardware,
                     Internet, Numbers, Path, Structure, Transport,
                     UnitSystem, Games, Cryptographic):
    pass


class Provider(LocaleDepProvider, CommonProvider):
    pass
