#!/bin/sh
/opt/venv/bin/python manage.py makemigrations --settings=merchant.settings.mc_info_web_api.settings
exec "$@"
