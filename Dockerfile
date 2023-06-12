# syntax=docker/dockerfile:1
#FROM alpine:3.16
#FROM ubuntu:22.04
#FROM python:3

# install app dependencies
#RUN apt-get update && apt-get install -y python3 python3-pip

FROM python:3-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY cloud_camp_test.py ./

CMD [ "python", "./cloud_camp_test.py" ]
