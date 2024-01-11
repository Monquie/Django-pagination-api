from django.db import models
import json


class Candidate(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)

    class Meta:
        indexes = [
            models.Index(fields=['department']),
            models.Index(fields=['position']),
            models.Index(fields=['location']),
            models.Index(fields=['status']),
            models.Index(fields=['company_name']),
        ]


class Organization(models.Model):
    text_id = models.CharField(max_length=100, unique=True, default=None)
    name = models.CharField(max_length=100, default=None)
    # Store configuration as a JSON string or use a JSONField
    """
    The Json value could be 0 (not enabled) / 1 (enabled)
    BE uses the Json value to determine which field should be returned
    Default value of this Json is 1 (all enabled)
    An Json configuration example
    {
        'name': 0, # not enabled
        'contact' : 1, # enabled
        'department' : 1,
        'status' : 1,
        ...
    }
    """
    candidate_display_config = models.TextField(
        help_text="JSON format of display configuration")

    class Meta:
        indexes = [
            models.Index(fields=['text_id']),
        ]

    def get_candidate_display_config(self):
        return json.loads(self.candidate_display_config)
