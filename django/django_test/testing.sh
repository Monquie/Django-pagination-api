#!/bin/sh
/opt/venv/bin/python manage.py test search.tests.tests --settings=djangoProject.settings --keepdb
exec "$@"