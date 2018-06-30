#!/bin/sh
python /usr/src/app/manage.py retry_deferred >> ~/cron_mail_deferred.log 2>&1