FROM python:3.6
MAINTAINER Yann Piquet <yann.piquet@epitech.eu>

RUN apt-get update
RUN apt-get install -y rabbitmq-server celeryd

COPY conf/* /etc/default/
RUN chmod 0640 /etc/default/celery*
COPY src/requirements.txt /requirements.txt

RUN pip3 install --upgrade pip
RUN pip3 install -r /requirements.txt

ADD src /app
WORKDIR /app

RUN chown -R celery .
RUN chmod +x start.sh

ENV PYTHONUNBUFFERED True

EXPOSE 80

CMD ./start.sh