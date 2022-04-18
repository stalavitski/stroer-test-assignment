from django.test import TestCase

from users.tests import factories


class UserTestCase(TestCase):
    # __str__ tests
    def test__str__returns_correct_value(self):
        user = factories.UserFactory.create()
        self.assertEqual(str(user), '{} {}'.format(user.first_name, user.last_name))
