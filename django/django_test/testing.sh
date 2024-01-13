#!/bin/sh
python manage.py test tests.merchant.mc_info_web_api.modules.tools.messaging.test_register_service --settings=tests.merchant.settings.mc_info_web_api.settings --keepdb