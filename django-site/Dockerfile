FROM python:alpine
MAINTAINER schietzsch@googlemail.com

RUN apk update \
  && apk add --update mariadb-dev libffi-dev build-base openssl\  
  && rm -rf /var/cache/apk/*

ADD run-15mins.sh /etc/periodic/15min/
ADD run-hourly.sh /etc/periodic/hourly/
ADD run-daily.sh /etc/periodic/daily/

WORKDIR /usr/src/app

ADD django-site/requirements.txt /usr/src/app/
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY django-site/ /usr/src/app/

RUN openssl req -new -newkey rsa:4096 -days 365 -nodes -x509 \
    -subj "/C=DE/ST=Bavaria/L=Munich/O=FF2k/CN=ff2k.net" \
    -keyout privkey.pem  -out cert.pem
    