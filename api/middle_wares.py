import logging
import re
import time
import uuid

from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)


class LoggingMiddleware(MiddlewareMixin):

    def __init__(self, get_response=None):
        super().__init__(get_response)

    def process_request(self, request):
        request.start_time = time.time()
        request.uuid = str(uuid.uuid4())
        body = re.sub(r"\s+", "", request.body.decode('utf-8'), flags=re.UNICODE)
        logger.debug(
            f"[{request.uuid}] request: {request.method} {request.get_full_path()}{request.GET.urlencode()} {body}")

    def process_response(self, request, response):
        elapsed_time = time.time() - request.start_time
        logger.debug(
            f"[{request.uuid}] response: {request.method} {request.get_full_path()}{request.GET.urlencode()} ({elapsed_time} s)")
        return response
