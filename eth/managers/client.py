from eth.custom_exceptions import RpcException
from eth.managers.requester import EthRequester


class EthClient:
    def __init__(self, requester=None) -> None:
        if requester is None:
            # config로 설정하도록 변경
            self.requester = EthRequester("10.0.1.163", 8898)
        else:
            self.requester = requester

    def get_block_number(self):
        response = self.requester.execute("eth_blockNumber")
        if response is None:
            raise RpcException
        return response

    def get_block_by_number(self, number: str):
        response = self.requester.execute("eth_getBlockByNumber", number, True)
        if response is None:
            raise RpcException
        return response

    def get_transaction_by_hash(self, tx_hash):
        response = self.requester.execute("eth_getTransactionByHash", tx_hash)
        if response is None:
            raise RpcException
        return response

    def get_transaction_receipt(self, tx_hash):
        response = self.requester.execute("eth_getTransactionReceipt", tx_hash)
        if response is None:
            raise RpcException
        return response
