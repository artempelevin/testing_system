FROM python:3.10
WORKDIR /usr/src/testing_system
COPY . .
RUN apt update
RUN pip3 install -r requirements.txt