#!/bin/sh

# Correr en dev enviroment
usermod -aG docker ${USER}

apt-get update \
    && apt-get upgrade -y \
    && apt-get -y install netcat python3-pip \
    && apt-get clean