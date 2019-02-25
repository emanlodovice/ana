from ana.serializers import RecordSerializer
from ana.models import Verb, Record

from django.test import TestCase
from django.contrib.auth import get_user_model


class RecordSerializerTestCase(TestCase):

    def test_validate_slug_existing(self):
        Verb.objects.create(slug='e')
        serializer = RecordSerializer(data={
            'verb_slug': 'e',
            'field1': '1',
            'field2': '2'
        })
        self.assertTrue(serializer.is_valid())

    def test_invalid_slug(self):
        serializer = RecordSerializer(data={
            'verb_slug': 'e e e',
            'field1': '1',
            'field2': '2'
        })
        self.assertFalse(serializer.is_valid())
        self.assertEqual('Invalid verb slug.',
                         serializer.errors['verb_slug'][0])

    def test_create_verb(self):
        serializer = RecordSerializer(data={
            'verb_slug': 'eee',
            'field1': '1',
            'field2': '2'
        })
        self.assertTrue(serializer.is_valid())
        serializer.save()
        self.assertEqual(1, Verb.objects.filter(slug='eee').count())
        self.assertEqual(1, Record.objects.filter(verb__slug='eee').count())

    def test_validate_with_verb_config(self):
        serializer = RecordSerializer(data={
            'verb_slug': 'page-view',
            'field1': '1',
            'field2': '2'
        })
        self.assertFalse(serializer.is_valid())
        User = get_user_model()
        user = User.objects.create_user(username='sample', password='qwe')
        serializer = RecordSerializer(data={
            'verb_slug': 'page-view',
            'field1': str(user.pk),
            'field2': '2'
        })
