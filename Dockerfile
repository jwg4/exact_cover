FROM etiennenapoleone/docker-python-poetry:3.7-rc

WORKDIR /tmp/working

COPY pyproject.toml .
COPY src .
COPY data/debug_data .
COPY tools/__init__.py .
COPY tools/debug.py .

RUN poetry install --no-virtualenv --no-dev

RUN poetry debug
