#!/bin/sh
/opt/venv/bin/python manage.py fake_data --settings=djangoProject.settings
/opt/venv/bin/python manage.py fake_org_data --settings=djangoProject.settings
exec "$@"
