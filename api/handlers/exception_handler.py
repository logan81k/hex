import logging

from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import exception_handler

from api.exceptions import ServiceException

logger = logging.getLogger(__name__)

'''
{
    "status": 401,
    "code": 2500,
    "message": "error message",
    "more_info": "http://www.bitberry.app/docs/errors/2500"
}
'''


def api_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
    print(f"response: {response}")
    if response is not None:
        # check if exception has dict items
        # if hasattr(exc.detail, 'items'):
        #     # remove the initial value
        #     response.data = {}
        #     errors = []
        #     for key, value in exc.detail.items():
        #         # append errors into the list
        #         errors.append("{} : {}".format(key, " ".join(value)))
        #
        #     # add property errors to the response
        #     response.data['errors'] = errors
        if isinstance(exc, ServiceException):
            # delete 
            del response.data["detail"]

            response.data["code"] = exc.code
            response.data["message"] = exc.message
            response.data["more_info"] = exc.more_info

        # serve status code in the response
        response.data['status'] = response.status_code

    return response
