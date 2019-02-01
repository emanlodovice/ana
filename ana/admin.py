from django.contrib import admin

from .models import Verb, Record


@admin.register(Verb)
class VerbAdmin(admin.ModelAdmin):
    pass


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    date_hierarchy = 'when'
    list_display = ('when', 'verb', 'field1')
    list_filter = ('verb',)
    search_fields = ('field1', 'field2')
