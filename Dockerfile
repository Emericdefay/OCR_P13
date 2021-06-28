FROM python:3.8
ENV PYTHINUNBUFFERED=1

RUN apt-get update 

WORKDIR /website
COPY requirements.txt /website/
RUN pip install -r requirements.txt
COPY . /website/