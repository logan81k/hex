from rest_framework import serializers

from api.models import Blocks, Transactions, Receipt


class IndexSerializer(serializers.Serializer):
    name = serializers.CharField(help_text='name')


class ExceptionSerializer(serializers.Serializer):
    name = serializers.CharField(help_text='name')
    error = serializers.CharField(help_text='error')


class BlocksModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blocks
        fields = '__all__'


class TransactionsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = '__all__'


class ReceiptModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = '__all__'
