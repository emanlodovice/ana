from django.core.validators import validate_slug, ValidationError

from rest_framework import serializers

from .models import Record, Verb


__all__ = ['VerbSerializer', 'RecordSerializer']


class VerbSerializer(serializers.ModelSerializer):

    class Meta:
        model = Verb
        fields = ('slug',)


class RecordSerializer(serializers.ModelSerializer):
    verb = serializers.StringRelatedField(read_only=True)
    labels = serializers.ReadOnlyField(source='verb.get_labels')
    verb_slug = serializers.CharField(required=True, write_only=True)

    def validate_verb_slug(self, value):
        try:
            verb = Verb.objects.get(slug=value)
        except Verb.DoesNotExist:
            try:
                validate_slug(value)
            except ValidationError:
                raise serializers.ValidationError('Invalid verb slug.')
            verb = Verb.objects.create(slug=value)
        return verb

    def validate(self, data):
        verb = data['verb_slug']

        config_class = verb.get_config_class()
        if not config_class:
            return data
        config = config_class(self.instance)
        try:
            data['field1'] = config.clean_field1(data['field1'])
        except ValidationError as e:
            raise serializers.ValidationError({'field1': e.message})

        try:
            data['field2'] = config.clean_field1(data['field2'])
        except ValidationError as e:
            raise serializers.ValidationError({'field2': e.message})
        return data

    class Meta:
        model = Record
        fields = ('field1', 'field2', 'verb', 'when',
                  'id', 'verb_slug', 'labels')

    def create(self, validated_data):
        verb = validated_data.pop('verb_slug')
        return Record.objects.create(verb=verb, **validated_data)
