import logging

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from api import serializers
from api.exceptions import OnlyAvailableException

logger = logging.getLogger(__name__)


class IndexView(GenericAPIView):
    serializer_class = serializers.IndexSerializer

    def get(self, request):
        print('yyyyyyyyyyyyyy')
        return Response(status=status.HTTP_200_OK, data={'message': 'Hello, HEX api'})

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        name = serializer.validated_data['name']
        return Response(status=status.HTTP_200_OK, data={'name': name})

    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        name = serializer.validated_data['name']
        return Response(status=status.HTTP_200_OK, data={'name': name})


class ExceptionView(APIView):

    def get(self, request, *args, **kwargs):
        raise OnlyAvailableException
        # return Response(status=status.HTTP_200_OK, data="raise exceptions")
