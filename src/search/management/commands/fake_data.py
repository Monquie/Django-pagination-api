import faker
from django.core.management.base import BaseCommand
import random
from search.models import Candidate, Organization


class Command(BaseCommand):
    help = 'Creates fake candidate data using Faker'

    def handle(self, *args, **options):
        fake = faker.Faker()

        for _ in range(1000):
            candidate = Candidate.objects.create(
                name=fake.name(),
                contact_info=fake.email(),
                department=fake.job(),
                position=fake.job(),
                location=fake.city(),
                # Keep status options limited
                status=random.choice(
                    ['Active', 'Not Started', 'Terminated']),
                company_name=fake.company()
            )

        self.stdout.write(self.style.SUCCESS(
            '1000 fake candidates created using Faker!'))
