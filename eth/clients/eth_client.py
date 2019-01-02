from eth.clients import EthRequester, RpcException
from eth.clients import BlockNumber


class EthClient:
    def __init__(self, requester=None) -> None:
        if requester is None:
            self.requester = EthRequester("10.0.1.163", 8898)
        else:
            self.requester = requester

    def get_block_number(self):
        response = self.requester.execute("eth_blockNumber")
        return BlockNumber(response)

    def get_block_by_number(self, number):
        response = self.requester.execute("eth_getBlockByNumber", hex(number), True)
        if response is None:
            raise RpcException()
        transactions = response["transactions"]
        return transactions



