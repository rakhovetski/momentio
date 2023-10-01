FROM python:3.10.13-alpine3.18

COPY . /backend
COPY ./requirements.txt backend/requirements.txt
WORKDIR /backend

RUN pip install -r requirements.txt

EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev

RUN adduser --disabled-password backend-user

USER backend-user