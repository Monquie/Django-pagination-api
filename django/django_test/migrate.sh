#!/bin/sh
/opt/venv/bin/python manage.py migrate --settings=djangoProject.settings
exec "$@"
