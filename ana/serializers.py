from rest_framework import serializers

from .models import Record, Verb


class VerbSerializer(serializers.ModelSerializer):

    class Meta:
        model = Verb
        fields = ('slug',)


class RecordSerializer(serializers.ModelSerializer):
    verb = serializers.StringRelatedField(read_only=True)
    verb_slug = serializers.CharField(required=True, write_only=True)

    def validate_verb_slug(self, value):
        try:
            verb = Verb.objects.get(slug=value)
        except Verb.DoesNotExist:
            raise serializers.ValidationError('Unregisted verb.')
        return verb

    class Meta:
        model = Record
        fields = ('field1', 'field2', 'verb', 'when', 'id', 'verb_slug')

    def create(self, validated_data):
        verb = validated_data.pop('verb_slug')
        return Record.objects.create(verb=verb, **validated_data)
