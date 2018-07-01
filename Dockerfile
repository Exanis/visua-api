FROM python:3.6 AS build-env
MAINTAINER Yann Piquet <yann.piquet@epitech.eu>

COPY src/requirements.txt /requirements.txt

RUN pip3 install --upgrade pip
RUN pip3 install -r /requirements.txt

ADD src /app
WORKDIR /app

CMD python manage.py migrate && gunicorn -w 4 visua.wsgi -b 0.0.0.0:80 --threads 4