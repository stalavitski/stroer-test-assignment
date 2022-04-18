from django.contrib.auth import get_user_model
from factory.declarations import SubFactory
from factory.django import DjangoModelFactory

from users import models

Administrator = get_user_model()


class AdministratorFactory(DjangoModelFactory):
    class Meta:
        model = Administrator
        django_get_or_create = ['username']

    username = 'test.admin'


class UserFactory(DjangoModelFactory):
    class Meta:
        model = models.User
        django_get_or_create = ['iban']

    first_name = 'Test First Name'
    last_name = 'Test Last Name'
    created_by = SubFactory(AdministratorFactory)
    iban = 'FR7630006000011234567890189'
