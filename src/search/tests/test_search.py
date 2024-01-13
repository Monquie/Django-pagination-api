from django.http import HttpRequest
from search.views import filter
import json


request = HttpRequest()
request.method = 'POST'
data = {'org_text_id': 'org-1', 'status': ['active', 'pending']}
request.data = json.dumps(data)
request.content_type = 'application/json'
response = filter(request)
