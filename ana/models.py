from django.db import models


class Verb(models.Model):
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.slug

    def __repr__(self):
        return f'<Verb: {self.slug}>'


class Record(models.Model):
    when = models.DateTimeField(auto_now_add=True)
    verb = models.ForeignKey(
        Verb, related_name='records', on_delete=models.SET_NULL, null=True)
    field1 = models.CharField(blank=True, max_length=255)
    field2 = models.CharField(blank=True, max_length=255)

    class Meta:
        ordering = ['pk']
