FROM python:3.9.7-slim-buster

WORKDIR /proyecto/src/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \

    && apt-get -y install gcc\
    && apt-get clean

RUN pip3 install --upgrade pip 
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .
