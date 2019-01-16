import logging

# Create your views here.
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from api import api_serializers
from api.api_response import ApiResponse
from api.exceptions import NotAllowedValueException
from api.helpers import preconditions
from api.models import Blocks, Transactions
from api.api_serializers import BlocksModelSerializer, TransactionsModelSerializer

logger = logging.getLogger(__name__)


class IndexView(GenericAPIView):
    serializer_class = api_serializers.IndexSerializer

    def get(self, request):
        return Response(status=status.HTTP_200_OK, data={'message': 'Hello, HEX api'})

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        print(serializer.validated_data)

        name = serializer.validated_data['name']
        return Response(status=status.HTTP_200_OK, data={'name': name})

    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        name = serializer.validated_data['name']
        return Response(status=status.HTTP_200_OK, data={'name': name})


class ExceptionView(GenericAPIView):
    serializer_class = api_serializers.ExceptionSerializer

    class Response:
        pass

    def get(self, request, *args, **kwargs):
        raise NotAllowedValueException('not_allowed')
        # return Response(status=status.HTTP_200_OK, data="raise exceptions")

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        print(serializer.validated_data)
        name = serializer.validated_data['name']
        error = serializer.validated_data['error']
        return Response(status=status.HTTP_200_OK, data={'name': name})


class BlocksView(GenericAPIView):

    def get(self, request, number):
        block = preconditions.exist_blocks_by_number(number)
        transactions = preconditions.exist_transactions_by_block_number(block.number)
        response = {
            'block': BlocksModelSerializer(block).data,
            # 'txs': [TransactionsModelSerializer(transaction).data for transaction in transactions]
            'tx_length': len(transactions)
        }
        return ApiResponse.ok(response)


class TransactionsView(GenericAPIView):

    def get(self, request, tx_hash):
        transaction = preconditions.exist_transaction_by_hash(tx_hash)
        transaction_serializer = TransactionsModelSerializer(transaction)
        return ApiResponse.ok(transaction_serializer.data)
