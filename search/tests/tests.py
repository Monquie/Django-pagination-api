from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from search.models import Candidate, Organization
import faker
import json


class FilterViewTest(TestCase):
    def setUp(self):
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

        Organization.objects.create(
            name="test",
            text_id='org-1',
            candidate_display_config=json.dumps(default_config))

        Candidate.objects.create(
            name='John Doe',
            contact_info=fake.email(),
            department='Engineering',
            position='developer',
            status='Active',
            company_name=fake.company())

        self.client = APIClient()

    def test_rate_limiting(self):
        # Assuming '_get_client_ip' and '_is_rate_limited' work based on client IP
        # Simulate multiple requests from the same IP
        for _ in range(11):  # Number of requests depending on your rate limit settings
            response = self.client.post(
                reverse('filter_candidate'), {}, format='json')

        # Assuming 429 is the status code for rate limit exceeded
        self.assertEqual(response.status_code, 429)

    # def test_invalid_input(self):
    #     # Send invalid data
    #     response = self.client.post(reverse('filter_view_name'), {'invalid': 'data'}, format='json')
    #     self.assertEqual(response.status_code, 400)  # Assuming 400 is for invalid inputs

    # def test_successful_filter(self):
    #     # Send valid data
    #     valid_data = {
    #         'org_text_id': 'org-1',
    #         'status': ['Active'],
    #         'department': 'Engineering',
    #         # ... other fields ...
    #     }
    #     response = self.client.post(reverse('filter_view_name'), valid_data, format='json')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTrue('list_candidate' in response.data)
