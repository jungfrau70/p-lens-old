# syntax=docker/dockerfile:1
FROM python:3.6.15-slim-buster

WORKDIR /app

COPY requirements-docker.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY config/hosts /etc/hosts
COPY telegraf-relay.py .

CMD [ "python3", "telegraf-relay.py"]