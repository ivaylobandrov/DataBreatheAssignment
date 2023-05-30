FROM python:3.10

# Configure Poetry
ENV POETRY_VERSION=1.4.2
ENV POETRY_VENV=/opt/poetry-venv

# Install poetry separated from system interpreter
RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

# Add `poetry` to PATH
ENV PATH="${PATH}:${POETRY_VENV}/bin"

WORKDIR /app

COPY /src /app/src
COPY pyproject.toml poetry.lock .env /app/

ENV PYTHONPATH=/app

RUN poetry install

EXPOSE 8000

CMD ["poetry", "run", "pytest"]

CMD ["poetry", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]