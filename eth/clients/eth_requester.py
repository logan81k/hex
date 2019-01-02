import json
import logging
import uuid

import requests

from eth.custom_exceptions import RpcException

logger = logging.getLogger(__name__)


class EthRequester:
    def __init__(self, ip, port):
        self._HEADERS = {'content-type': 'application/json'}
        self._rpc_url = f"http://{ip}:{port}"

    def _build_payload(self, method, params, kwargs):

        request_id = str(uuid.uuid4())
        payload = {
            "method": method,
            "id": request_id,
            "jsonrpc": "2.0"
        }

        if params:
            if len(params) == 1 and (isinstance(params[0], dict) or isinstance(params[0], list)):
                payload['params'] = params[0]
            else:
                payload['params'] = params
        elif kwargs:
            payload['params'] = kwargs
        else:
            payload['params'] = []

        return request_id, payload

    def execute(self, method, *params, **kwargs):
        request_id, payload = self._build_payload(method, params, kwargs)

        response = requests.post(self._rpc_url, data=json.dumps(payload), headers=self._HEADERS).json()
        if response.get('error') is not None:
            raise RpcException(response['error']['message'], response['error']['code'])

        if response['id'] != request_id:
            msg = f"RPC response's id({response['id']}) not equal to request id({request_id})"
            logger.error(msg)
            raise RpcException(msg)

        return response['result']
