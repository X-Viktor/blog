FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY Pipfile Pipfile.lock ./
RUN pip install --upgrade pip && pip install pipenv && pipenv install --dev --system && pip install Django && pip install django-environ

COPY . .

EXPOSE 8000