# How to contribute

## Dependencies

We use [`poetry`](https://github.com/sdispater/poetry) to manage the dependencies.

To install them you would need to run two commands:

```bash
poetry install
```

## Tests

We use `pytest`, `mypy`, and `flake8` for quality control.
To run all tests:

```bash
pytest
```

We also use [`wemake-python-styleguide`](https://github.com/wemake-services/wemake-python-styleguide) to lint our `python` code.

To run linting:

```bash
flake8 mimesis_factory.py tests
```

And to type check your code:

```bash
mypy mimesis_factory.py
```

Make sure you have followed all the steps before submitting your PR.


## Before submitting

Before submitting your code please do the following steps:

1. Run `pytest` to make sure everything was working before
2. Add any changes you want
3. Adds tests for the new changes
4. Edit documentation if you have changed something significant
5. Run `pytest` again to make sure it is still working


## Other help

You can contribute by spreading a word about this library.
It would also be a huge contribution to write
a short article on how you are using this project.
What are your best-practices?
