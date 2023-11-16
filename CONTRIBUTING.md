# Contributing

## set up a test environment

from a fresh / empty Python environment:

```bash
### poetry is the swiss army knife of python dependency management
pip install poetry
### install the dependencies and the current package
poetry install
### run the tests
poetry run test
```

you can also do

```bash
# run quicktest only
poetry run quicktest
# Python repl with the package loaded
poetry run python
# same with ipthon (may need explicit install
poetry run ipython
```
