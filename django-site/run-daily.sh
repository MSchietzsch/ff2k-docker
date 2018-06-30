#!/bin/sh
python /usr/src/app/manage.py purge_mail_log 7 >> ~/cron_mail_purge.log 2>&1
