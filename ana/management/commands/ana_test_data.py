from ana.models import Verb, Record

from django.core.management.base import BaseCommand
from django.utils import timezone

from random import randint

from uuid import uuid4


class Command(BaseCommand):
    help = 'Generate test records for ana app'

    def add_arguments(self, parser):
        parser.add_argument(
            '-s', '--slug', type=str, help='Verb slug for the records',
            default='page-view', nargs='?')

        parser.add_argument(
            '-c', '--count', type=int, help='Verb slug for the records',
            default=100, nargs='?')

    def handle(self, *args, **kwargs):
        verb = Verb.objects.get_or_create(slug=kwargs['slug'])[0]
        for x in range(0, kwargs['count']):
            when = timezone.now() - timezone.timedelta(hours=randint(0, 1000))
            user = uuid4().__str__()
            rec = Record.objects.create(verb=verb, field1=user, field2='/')
            rec.when = when
            rec.save(update_fields=['when'])
            print((x + 1) / kwargs['count'] * 100, '%')
