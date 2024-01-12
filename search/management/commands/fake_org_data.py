import faker
from django.core.management.base import BaseCommand
# Replace 'your_app' with the actual app name
import random
from search.models import Candidate, Organization
import json


class Command(BaseCommand):
    help = 'Creates fake candidate data using Faker'

    def handle(self, *args, **options):
        fake = faker.Faker()

        default_config = dict(
            name=1,
            contact_info=1,
            department=1,
            position=1,
            location=1,
            status=1,
            company_name=1,
        )

        test_config = dict(
            name=0,
            contact_info=0,
            department=1,
            position=1,
            location=1,
            status=0,
            company_name=0,
        )

        Organization.objects.create(
            text_id='org-3', name='ting', candidate_display_config=json.dumps(default_config))

        Organization.objects.create(
            text_id='org-2', name='ting_ting', candidate_display_config=json.dumps(test_config))
        self.stdout.write(self.style.SUCCESS(
            '2 fake organization created using Faker!'))
