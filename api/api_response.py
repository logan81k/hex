from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response


class ApiResponse:
    @staticmethod
    def response(data=None, http_status=status.HTTP_200_OK):
        if not data:
            return Response(status=http_status)
        return JsonResponse(data, status=http_status)

    @staticmethod
    def ok(data=None):
        return ApiResponse.response(data=data)

    @staticmethod
    def not_found(data=None):
        return ApiResponse.response(data=data, http_status=status.HTTP_404_NOT_FOUND)

    @staticmethod
    def bad_request(data=None):
        return ApiResponse.response(data=data, http_status=status.HTTP_400_BAD_REQUEST)
