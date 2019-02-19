from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import reverse

from ana.models import Record


User = get_user_model()


class AccessControlRecordsEndpointTestCase(TestCase):

    url = reverse('ana:record-list')
    payload = {
        'verb_slug': 'eee',
        'field1': '1',
        'field2': '2'
    }

    def setUp(self):
        self.user = User.objects.create_user(
            username='tester', password='testertester')

    def test_create_record(self):
        # anyone can access api to add a record
        response = self.client.post(self.url, self.payload)
        self.assertEqual(201, response.status_code)
        self.assertTrue(Record.objects.filter(
            verb__slug='eee', field1='1', field2='2'))

    def test_get_data_not_authenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(403, response.status_code)

    def test_get_data_no_permission(self):
        self.client.login(username='tester', password='testertester')
        response = self.client.get(self.url)
        self.assertEqual(403, response.status_code)

    def test_has_access(self):
        perm = Permission.objects.get(codename='can_access_ana_api_analytics')
        self.user.user_permissions.add(perm)
        self.client.login(username='tester', password='testertester')
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)
