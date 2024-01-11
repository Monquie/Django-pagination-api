from django.views.decorators.http import require_http_methods
from django.core.cache import cache
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from search.models import Candidate, Organization
import json


# @require_http_methods(["POST"])
@api_view(['POST'])
def filter(request: Request) -> Response:
    class InputSerializer(serializers.Serializer):
        department = serializers.CharField(required=False, max_length=100)
        position = serializers.CharField(required=False, max_length=100)
        location = serializers.CharField(required=False, max_length=100)
        company_name = serializers.CharField(required=False, max_length=100)
        status = serializers.ListField(
            required=False, child=serializers.CharField())
        cursor = serializers.IntegerField(required=False)  # used in paging
        org_text_id = serializers.CharField(required=True, max_length=100)

    # check rate limitings
    client_ip = _get_client_ip(request)
    if _is_rate_limited(client_ip):
        return _build_response(
            success=False,
            response_code='EXCEED_NUMBER_OF_REQUEST',
            errors='ERROR',
        )

    # Validate input
    serializer = InputSerializer(data=request.data)
    if not serializer.is_valid():
        print(request.data)
        print(type(request.data))
        print("Invalid request")
        return _build_response(
            success=False,
            response_code='INVALID_REQUEST_INPUTS',
            errors=serializer.errors,
        )
    valid_data = serializer.validated_data

    # Extract filter criteria
    # valid_data = request.json()
    department = valid_data.get('department')
    position = valid_data.get('position')
    location = valid_data.get('location')
    company_name = valid_data.get('company_name')
    status = valid_data.get('status')
    cursor = valid_data.get('cursor')
    org_text_id = valid_data.get('org_text_id')

    # Build the query
    query = {}
    if department:
        query['department'] = department
    if position:
        query['position'] = position
    if location:
        query['location'] = location
    if company_name:
        query['company_name'] = company_name
    if status:
        query['status__in'] = status  # Use __in
    if cursor:
        query['id__gt'] = cursor  # use cursor based paging

    # Execute the query and limit to 300 results
    candidates = Candidate.objects.filter(
        **query)[:300]  # limit display 6 pages

    # Get organization dynamic columns
    try:
        organization = Organization.objects.get(text_id=org_text_id)
        org_config = organization.get_candidate_display_config()
    except Organization.DoesNotExist:
        print("Not exxist")
        print(org_text_id)
        return _build_response(
            success=False,
            response_code='INVALID_ORGANIZATION_INPUTS',
        )

    # Serialize the results
    results = [
        dict(
            name=candidate.name if org_config['name'] == 1 else None,
            contact_info=candidate.contact_info if org_config['contact_info'] == 1 else None,
            department=candidate.department if org_config['department'] == 1 else None,
            position=candidate.position if org_config['position'] == 1 else None,
            location=candidate.location if org_config['location'] == 1 else None,
            status=candidate.status if org_config['status'] == 1 else None,
            company_name=candidate.company_name if org_config['company_name'] == 1 else None,
        )
        for candidate in candidates
    ]

    return _build_response(
        success=True,
        data=dict(
            list_candidate=results
        ),
    )


def _is_rate_limited(ip):
    # Check and update rate limit count
    cache_key = f'rate_limit_{ip}'
    count = cache.get(cache_key, 0)
    if count >= 10:
        return True
    cache.set(cache_key, count + 1, timeout=1)  # Timeout set to 1 second
    return False


def _get_client_ip(request: Request):
    meta = request.META
    if 'HTTP_X_FORWARDED_FOR' in meta:
        ip = meta['HTTP_X_FORWARDED_FOR'].split(',')[0]
    elif 'HTTP_X_REAL_IP' in meta:
        ip = meta['HTTP_X_REAL_IP']
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def _build_response(
    success,
    data=None,
    errors=None,
    messages=None,
    response_code=None,
    http_status=200,
    *args,
    **kwargs
):
    response_data = {'success': success}

    if data is not None:
        response_data['data'] = data

    if errors is not None:
        response_data['errors'] = errors

    if messages is not None:
        response_data['messages'] = messages

    if response_code is not None:
        response_data['response_code'] = response_code

    return Response(data=response_data, status=http_status)
