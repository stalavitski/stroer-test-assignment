from rest_framework import serializers

from users import models


class UserSerializer(serializers.ModelSerializer):
    iban = serializers.CharField(trim_whitespace=True)

    class Meta:
        exclude = ['created_by']
        model = models.User
