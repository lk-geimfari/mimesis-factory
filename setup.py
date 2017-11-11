from distutils.core import setup

from mimesis_factory import __version__

setup(
    name='mimesis_factory',
    version=__version__,
    packages=['mimesis_factory'],
    url='https://github.com/mimesis-lab/mimesis-factory',
    license='MIT',
    author='Sobolev Nikita, Likid Geimfari',
    description='Mimesis integration with factory_boy'
)
