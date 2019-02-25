from django.db import models
from django.core.validators import ValidationError
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _


FIELD_CONFIG = {}


class Verb(models.Model):
    slug = models.SlugField(unique=True)

    def get_config_class(self):
        if self.slug in FIELD_CONFIG:
            return FIELD_CONFIG[self.slug]
        return None

    def get_labels(self):
        config_class = self.get_config_class()
        if not config_class:
            return {
                'field1': 'field1',
                'field2': 'field2'
            }
        return config_class.get_labels()

    def __str__(self):
        return self.slug

    def __repr__(self):
        return self.slug


class Record(models.Model):
    when = models.DateTimeField(auto_now_add=True)
    verb = models.ForeignKey(
        Verb, related_name='records', on_delete=models.SET_NULL, null=True)
    field1 = models.CharField(blank=True, max_length=255)
    field2 = models.CharField(blank=True, max_length=255)

    class Meta:
        ordering = ['pk']
        permissions = (
            ('can_access_ana_api_analytics', 'Can access analytics api'),
            ('can_access_ana_dashboard', 'Can view analytics dashboard')
        )


class RecordModifier(type):

    def __new__(cls, name, bases, ns):
        new_cls = super().__new__(cls, name, bases, ns)
        FIELD_CONFIG[ns['verb']] = new_cls
        return new_cls


class VerbConfig(metaclass=RecordModifier):
    verb = None
    field1_label = None
    field2_label = None

    def __init__(self, instance):
        self.instance = instance

    def clean_field1(self, value):
        return value

    def clean_field2(self, value):
        return value

    @classmethod
    def get_labels(cls):
        return {
            'field1': cls.field1_label,
            'field2': cls.field2_label
        }


class PageViewConfig(VerbConfig, metaclass=RecordModifier):
    verb = 'page-view'
    field1_label = 'user'
    field2_label = 'url'

    def clean_field1(self, value):
        User = get_user_model()
        if value.isdigit() and not User.objects.filter(pk=value).exists():
            raise ValidationError(_('User does not exist!'))
        return value
