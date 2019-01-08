from rest_framework import serializers


class IndexSerializer(serializers.Serializer):
    name = serializers.CharField(help_text='name')


class ExceptionSerializer(serializers.Serializer):
    name = serializers.CharField(help_text='name')
    error = serializers.CharField(help_text='error')
