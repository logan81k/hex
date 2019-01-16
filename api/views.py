import logging

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from api import serializers
from api.exceptions import NotAllowedValueException

logger = logging.getLogger(__name__)


class IndexView(GenericAPIView):
    serializer_class = serializers.IndexSerializer

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
    serializer_class =  serializers.ExceptionSerializer

    class Response:
        pass

    def get(self, request, *args, **kwargs):
        raise NotAllowedValueException
        # return Response(status=status.HTTP_200_OK, data="raise exceptions")

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        print(serializer.validated_data)
        name = serializer.validated_data['name']
        error = serializer.validated_data['error']
        return Response(status=status.HTTP_200_OK, data={'name': name})
