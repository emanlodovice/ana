from ana.models import Verb

from django.test import TestCase


class VerbModelTestCase(TestCase):

    def test_model_str_repr(self):
        verb = Verb.objects.create(slug='page-hit')
        self.assertEqual(str(verb), verb.slug)
