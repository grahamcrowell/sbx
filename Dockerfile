FROM python:3.8-slim-buster

RUN pip install pip --upgrade
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
