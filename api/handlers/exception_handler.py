import logging

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
        if isinstance(exc, ServiceException):
            # delete 
            del response.data["detail"]

            response.data["code"] = exc.code
            response.data["message"] = exc.message
            response.data["more_info"] = exc.more_info

            # serve status code in the response
        response.data['status'] = response.status_code

    return response
