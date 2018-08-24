FROM python:3.6
MAINTAINER Yann Piquet <yann.piquet@epitech.eu>

COPY src/requirements.txt /requirements.txt

RUN pip3 install --upgrade pip
RUN pip3 install -r /requirements.txt

ADD src /app
WORKDIR /app

RUN chmod +x start.sh

ENV PYTHONUNBUFFERED True

CMD ./start.sh