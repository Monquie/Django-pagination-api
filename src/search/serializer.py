from rest_framework import serializers


class InputSerializer(serializers.Serializer):
    department = serializers.CharField(required=False, max_length=100)
    position = serializers.CharField(required=False, max_length=100)
    location = serializers.CharField(required=False, max_length=100)
    company_name = serializers.CharField(required=False, max_length=100)
    status = serializers.ListField(
        required=False, child=serializers.CharField())
    cursor = serializers.CharField(
        required=False, allow_blank=True)  # used in paging
    org_text_id = serializers.CharField(required=True, max_length=100)
