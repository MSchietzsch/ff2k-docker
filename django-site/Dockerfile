FROM python:alpine
MAINTAINER schietzsch@googlemail.com

RUN apk update \
  && apk add --update mariadb-dev libffi-dev build-base \  
  && rm -rf /var/cache/apk/*

ADD run-15mins.sh /etc/periodic/15min/
ADD run-hourly.sh /etc/periodic/hourly/
ADD run-daily.sh /etc/periodic/daily/

WORKDIR /usr/src/app

ADD django-site/requirements.txt /usr/src/app/
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY django-site/ /usr/src/app/
