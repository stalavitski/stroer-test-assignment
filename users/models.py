from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class Administrator(AbstractUser):
    pass


class User(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    iban = models.CharField(
        max_length=32,
        validators=[
            # 11 chars for Norway BBAN (the smallest), 30 chars is max amount according to specification
            RegexValidator(
                regex='^[A-Z]{2}[0-9]{2}[A-Z0-9]{11,30}$',
                message='IBAN is invalid. Value should consist only from alphanumeric characters',
                code='invalid_iban'
            ),
        ]
    )

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
