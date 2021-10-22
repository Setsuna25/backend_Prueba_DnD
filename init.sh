#!/bin/sh


apt-get update \
    && apt-get upgrade -y \
    && apt-get -y install netcat python3-pip \
    && apt-get clean