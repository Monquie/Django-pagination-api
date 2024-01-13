#!/bin/sh

python3 -m venv /opt/venv
/opt/venv/bin/pip install --upgrade pip
/opt/venv/bin/pip install -r /backenddjango/requirements.txt
# sh /wait-for-db.sh

cd /backenddjango
# source /opt/venv/bin/activate
# while true
# do
#     sleep 1
# done

/opt/venv/bin/python manage.py runserver 0.0.0.0:8000 --settings=djangoProject.settings
