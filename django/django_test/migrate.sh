#!/bin/sh
/opt/venv/bin/python manage.py migrate --settings=merchant.settings.mc_info_web_api.settings --database=mc_info
exec "$@"
