from rest_framework.exceptions import APIException


class ServiceException(APIException):
    status_code = 400

    def __init__(self, code=None, message=None):
        super().__init__(code, "허용되지 않는 값입니다.")
        self.code = code
        self.message = message
        self.more_info = f"https://www.bitberry.app/docs/errors/{self.code}"


class NotAllowedValueException(ServiceException):
    def __init__(self, v):
        super().__init__(1234, f"{v}는 허용되지 않는 값입니다.")


class BlockDoesNotExistException(ServiceException):
    def __init__(self, query):
        super().__init__(f"{query}에 해당하는 block은 존재하지 않습니다.")


class TransactionDoesNotExistException(ServiceException):

    def __init__(self, query):
        super().__init__(f"{query}에 해당하는 transaction은 존재하지 않습니다.")
