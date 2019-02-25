from ana.models import Verb, FIELD_CONFIG, PageViewConfig

from django.test import TestCase
from django.core.validators import ValidationError
from django.contrib.auth import get_user_model


class VerbConfigTestCase(TestCase):

    def test_registration_of_config(self):
        self.assertTrue(FIELD_CONFIG['page-view'], PageViewConfig)


class VerbModelTestCase(TestCase):

    def test_model_str_repr(self):
        verb = Verb.objects.create(slug='page-hit')
        self.assertEqual(str(verb), verb.slug)

    def test_get_config_class(self):
        verb = Verb(slug='dummy-slug')
        self.assertIsNone(verb.get_config_class())
        verb.slug = 'page-view'
        self.assertEqual(PageViewConfig, verb.get_config_class())

    def test_get_labels(self):
        verb = Verb(slug='dummy-slug')
        self.assertEqual(
            {
                'field1': 'field1',
                'field2': 'field2'
            },
            verb.get_labels()
        )
        verb.slug = 'page-view'
        self.assertEqual(
            {
                'field1': 'user',
                'field2': 'url'
            },
            verb.get_labels()
        )


class PageViewConfigTestCase(TestCase):

    def setUp(self):
        self.config = PageViewConfig(None)

    def test_not_int(self):
        self.assertEqual('a', self.config.clean_field1('a'))

    def test_int(self):
        with self.assertRaises(ValidationError):
            self.config.clean_field1('1')
        User = get_user_model()
        user = User.objects.create_user(username='sample', password='qwe')
        self.assertEqual(str(user.pk), self.config.clean_field1(str(user.pk)))
