from rest_framework import serializers


class ConvertTokenSerializer(serializers.Serializer):
    client_id = serializers.CharField()
    client_secret = serializers.CharField()
    token = serializers.CharField()
