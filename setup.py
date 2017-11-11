from distutils.core import setup

import mimesis_factory

setup(
    name='mimesis_factory',
    version=mimesis_factory.__version__,
    packages=['mimesis_factory'],
    url='https://github.com/mimesis-lab/mimesis-factory',
    license='MIT',
    author='Sobolev Nikita, Likid Geimfari',
    description='Mimesis integration with factory_boy',
    install_requires=[
        'mimesis',
        'factory-boy',
    ],
)
