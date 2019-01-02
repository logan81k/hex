from django.http import HttpResponse

# Create your views here.
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from api import serializers


class IndexView(GenericAPIView):
    serializer_class = serializers.IndexSerializer

    def get(self, request):
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

