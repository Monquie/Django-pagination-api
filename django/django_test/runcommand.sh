#!/bin/sh
/opt/venv/bin/python manage.py generate_team paykick --settings=developer.developer_web_api.settings
/opt/venv/bin/python manage.py generate_project 'F236B0061B8F462297202FFA58A3915E' 'tingpayapp' --settings=developer.developer_web_api.settings
/opt/venv/bin/python manage.py cloud_messaging_create_app 'C1DC7A65D3D04B2D803A8F301499E628' chatapp --settings=developer.developer_web_api.settings
/opt/venv/bin/python manage.py cloud_messaging_generate_api_client 'C1DC7A65D3D04B2D803A8F301499E628' --settings=developer.developer_web_api.settings
exec "$@"
