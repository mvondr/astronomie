# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY /python-docker/requirements.txt .
RUN pip3 install -r requirements.txt

COPY /python-docker .

EXPOSE 5000

CMD [ "python3", "app.py"]
