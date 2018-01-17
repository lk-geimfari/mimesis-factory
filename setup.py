from distutils.core import setup

setup(
    name='mimesis_factory',
    version='0.0.2',
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
