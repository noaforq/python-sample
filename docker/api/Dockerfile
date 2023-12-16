FROM python:3.10

WORKDIR /app

COPY ./pyproject.toml .
COPY ./poetry.lock .

RUN pip install poetry>=1.2.0
RUN poetry config virtualenvs.create false
RUN poetry install
