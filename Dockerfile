FROM python:3.7.1-alpine3.8
LABEL maintainer "ricardobchaves6@gmail.com"

WORKDIR /api

COPY . /api

RUN pip install --upgrade pip==18.1 && \
    pip install -r requirements_dev.txt && \
    pip install -r /api/tests/requirements.txt
