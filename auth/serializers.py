from rest_framework import serializers


class ConvertTokenSerializer(serializers.Serializer):
    backend = serializers.CharField(default='google-oauth2', initial='google-oauth2')
    grant_type = serializers.CharField(default='convert_token', initial='convert_token')
    client_id = serializers.CharField()
    client_secret = serializers.CharField()
    token = serializers.CharField()
