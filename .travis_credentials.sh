#!/usr/bin/env bash

cat > haproxy/aws-config << EOL
[default]
aws_access_key_id=${aws_access_key_id-haproxy}
aws_secret_access_key=${aws_secret_access_key-haproxy}
EOL

cat > django-site/django-site/.env << EOL
[default]
SECRET_KEY=${SECRET_KEY}
DB_HOST=pgsql
DB_NAME=ff2kdb
DB_USER=postgres
DB_PASSWORD=some_password
DB_PORT=5432
AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}
AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}
AWS_STORAGE_BUCKET_NAME=ff2k-static
EMAIL_HOST = email-smtp.eu-west-1.amazonaws.com
EMAIL_PORT = 587
EMAIL_HOST_USER=${EMAIL_HOST_USER}
EMAIL_HOST_PASSWORD={$EMAIL_HOST_PASSWORD}
EOL
