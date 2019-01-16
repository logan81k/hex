from eth.managers.client import EthClient
from eth.managers.requester import EthRequester
from eth.managers.responses import BlockNumber, Transaction, Receipt, Block


class EthManager:
    def __init__(self) -> None:
        self.client = EthClient(EthRequester("10.0.1.163", 8898))

    def get_block_number(self):
        response = self.client.get_block_number()
        return BlockNumber(response)

    def get_block_by_number(self, number: str):
        response = self.client.get_block_by_number(number)
        return Block(response)

    def get_transaction_by_hash(self, tx_hash):
        response = self.client.get_transaction_by_hash(tx_hash)
        return Transaction(response)

    def get_transaction_receipt(self, tx_hash):
        response = self.client.get_transaction_receipt(tx_hash)
        return Receipt(response)
