# Base image
FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.8

ENV APP_ENV=production \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=0.12.11

# Don't run uwsgi as root
RUN echo 'uid = uwsgi' >> /app/uwsgi.ini
RUN echo 'gid = uwsgi' >> /app/uwsgi.ini

# System deps:
RUN pip install "poetry==${POETRY_VERSION}"

# Copy only requirements to cache them in docker layer
WORKDIR /app
COPY poetry.lock pyproject.toml /app/

# Project initialization:
RUN poetry config settings.virtualenvs.create false \
    && poetry install $(test "${APP_ENV}" == production && echo "--no-dev") --no-interaction --no-ansi

# Creating folders, and files for a project:
COPY ./pythonclub /app