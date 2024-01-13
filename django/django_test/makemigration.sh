#!/bin/sh
/opt/venv/bin/python manage.py makemigrations --settings=djangoProject.settings
exec "$@"
