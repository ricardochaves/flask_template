FROM python:3.7.1-alpine3.8
LABEL maintainer "ricardobchaves6@gmail.com"

WORKDIR /api

ADD . /api

RUN pip install --upgrade pip && \
    pip install -r requirements_dev.txt
