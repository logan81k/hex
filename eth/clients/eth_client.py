from eth.clients.eth_requester import EthRequester
from eth.clients.responses import BlockNumber, Block
from eth.custom_exceptions import RpcException


class EthClient:
    def __init__(self, requester=None) -> None:
        if requester is None:
            self.requester = EthRequester("10.0.1.163", 8898)
        else:
            self.requester = requester

    def get_block_number(self):
        response = self.requester.execute("eth_blockNumber")
        if response is None:
            raise RpcException
        return BlockNumber(response)

    def get_block_by_number(self, block_number: str):
        response = self.requester.execute("eth_getBlockByNumber", block_number, True)
        if response is None:
            raise RpcException
        return Block(response)





