#!/bin/sh
python /usr/src/app/manage.py send_mail >> ~/cron_mail.log 2>&1