FROM python:3.7-alpine

WORKDIR /proyecto/src/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk  update \
    && apk add g++ \
    && apk add  gcc \
    && apk add  python3-dev \
    && apk add  libevent-dev \
    && apk add  libffi-dev \
    && apk add  musl-dev \
    && apk add  postgresql-dev

RUN pip3 install --upgrade  pip 
COPY ./requirements.txt .
RUN pip3 install -r  requirements.txt

COPY . .
