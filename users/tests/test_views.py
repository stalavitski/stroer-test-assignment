import json

from rest_framework.test import APITestCase

from users.tests import factories


class UserViewSetTestCase(APITestCase):
    URL = '/users/users/'
    DETAIL_URL = URL+'{}/'

    # list tests
    def test__list__returns_user_data__for_administrator(self):
        administrator = factories.AdministratorFactory.create()
        self.client.force_authenticate(user=administrator)
        user = factories.UserFactory.create(created_by=administrator)
        response = self.client.get(self.URL)
        content = json.loads(response.content.decode('utf-8'))
        self.assertEqual(len(content), 1)
        self.assertDictEqual(content[0], {
            'id': user.id,
            'iban': user.iban,
            'first_name': user.first_name,
            'last_name': user.last_name,
        })

    def test__list__doesnt_return_user_data__for_wrong_administrator(self):
        administrator = factories.AdministratorFactory.create()
        administrator2 = factories.AdministratorFactory.create(username='test.admin2')
        self.client.force_authenticate(user=administrator)
        factories.UserFactory.create(created_by=administrator2)
        response = self.client.get(self.URL)
        content = json.loads(response.content.decode('utf-8'))
        self.assertEqual(len(content), 0)

    def test__list__raises_401_error__when_unauthenticated(self):
        factories.UserFactory.create()
        response = self.client.get(self.URL)
        self.assertEqual(response.status_code, 401)

    # retrieve tests
    def test__retrieve__returns_user_data__for_administrator(self):
        administrator = factories.AdministratorFactory.create()
        self.client.force_authenticate(user=administrator)
        user = factories.UserFactory.create(created_by=administrator)
        response = self.client.get(self.DETAIL_URL.format(user.id))
        content = json.loads(response.content.decode('utf-8'))
        self.assertDictEqual(content, {
            'id': user.id,
            'iban': user.iban,
            'first_name': user.first_name,
            'last_name': user.last_name,
        })

    def test__retrieve__returns_404_error__for_wrong_administrator(self):
        administrator = factories.AdministratorFactory.create()
        administrator2 = factories.AdministratorFactory.create(username='test.admin2')
        self.client.force_authenticate(user=administrator)
        user = factories.UserFactory.create(created_by=administrator2)
        response = self.client.get(self.DETAIL_URL.format(user.id))
        json.loads(response.content.decode('utf-8'))
        self.assertEqual(response.status_code, 404)

    def test__retrieve__raises_401_error__when_unauthenticated(self):
        user = factories.UserFactory.create()
        response = self.client.get(self.DETAIL_URL.format(user.id))
        self.assertEqual(response.status_code, 401)

    # post tests
    def test__post__returns_user_data__for_administrator(self):
        administrator = factories.AdministratorFactory.create()
        self.client.force_authenticate(user=administrator)
        response = self.client.post(self.URL, data={
            'first_name': 'Test first name',
            'last_name': 'Test last name',
            'iban': 'IE12 BOFI 9000 0112 3456 78',
        })
        self.assertEqual(response.status_code, 201)

    def test__post__raises_401_error__when_unauthenticated(self):
        user = factories.UserFactory.create()
        response = self.client.post(self.URL)
        self.assertEqual(response.status_code, 401)

    # put tests
    def test__put__returns_user_data__for_administrator(self):
        administrator = factories.AdministratorFactory.create()
        self.client.force_authenticate(user=administrator)
        user = factories.UserFactory.create(created_by=administrator)
        first_name = 'Test first name'
        response = self.client.put(self.DETAIL_URL.format(user.id), data={
            'first_name': first_name,
            'last_name': user.last_name,
            'iban': user.iban,
        })
        content = json.loads(response.content.decode('utf-8'))
        self.assertDictEqual(content, {
            'id': user.id,
            'iban': user.iban,
            'first_name': first_name,
            'last_name': user.last_name,
        })

    def test__put__returns_404_error__for_wrong_administrator(self):
        administrator = factories.AdministratorFactory.create()
        administrator2 = factories.AdministratorFactory.create(username='test.admin2')
        self.client.force_authenticate(user=administrator)
        user = factories.UserFactory.create(created_by=administrator2)
        first_name = 'Test first name'
        response = self.client.put(self.DETAIL_URL.format(user.id), data={
            'first_name': first_name,
            'last_name': user.last_name,
            'iban': user.iban,
        })
        json.loads(response.content.decode('utf-8'))
        self.assertEqual(response.status_code, 404)

    def test__put__raises_401_error__when_unauthenticated(self):
        user = factories.UserFactory.create()
        first_name = 'Test first name'
        response = self.client.put(self.DETAIL_URL.format(user.id), data={
            'first_name': first_name,
            'last_name': user.last_name,
            'iban': user.iban,
        })
        self.assertEqual(response.status_code, 401)

    # patch tests
    def test__patch__returns_user_data__for_administrator(self):
        administrator = factories.AdministratorFactory.create()
        self.client.force_authenticate(user=administrator)
        user = factories.UserFactory.create(created_by=administrator)
        first_name = 'Test first name'
        response = self.client.patch(self.DETAIL_URL.format(user.id), data={
            'first_name': first_name,
        })
        content = json.loads(response.content.decode('utf-8'))
        self.assertDictEqual(content, {
            'id': user.id,
            'iban': user.iban,
            'first_name': first_name,
            'last_name': user.last_name,
        })

    def test__patch__returns_404_error__for_wrong_administrator(self):
        administrator = factories.AdministratorFactory.create()
        administrator2 = factories.AdministratorFactory.create(username='test.admin2')
        self.client.force_authenticate(user=administrator)
        user = factories.UserFactory.create(created_by=administrator2)
        first_name = 'Test first name'
        response = self.client.patch(self.DETAIL_URL.format(user.id), data={
            'first_name': first_name,
        })
        json.loads(response.content.decode('utf-8'))
        self.assertEqual(response.status_code, 404)

    def test__patch__raises_401_error__when_unauthenticated(self):
        user = factories.UserFactory.create()
        first_name = 'Test first name'
        response = self.client.patch(self.DETAIL_URL.format(user.id), data={
            'first_name': first_name,
        })
        self.assertEqual(response.status_code, 401)
