from rest_framework import status
from rest_framework.exceptions import APIException


class ServiceException(APIException):
   status_code = 400

   def __init__(self, code=None, message=None):
        super().__init__(code, "허용되지 않는 값입니다.")
        self.code = code
        self.message = message
        self.more_info = f"https://www.bitberry.app/docs/errors/{self.code}"


class OnlyAvailableException(ServiceException):
    def __init__(self):
        super().__init__(1234, "허용되지 않는 값입니다.")




