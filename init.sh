#!/bin/sh

# Correr en dev enviroment
usermod -aG docker ${USER}

apt-get update \
    && apt-get upgrade -y \
    && apt-get -y install python3-pip libpq-dev python-dev netcat \
    && apt-get clean