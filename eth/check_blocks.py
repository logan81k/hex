import os

from web3 import Web3

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hex.settings")
import django

django.setup()

import logging
from api.handlers.decorators import run_handler
from eth.managers.manager import EthManager
from api.models import LastBlock, Blocks, Transactions, Receipt

logger = logging.getLogger(__name__)


class CheckBlock:

    def __init__(self) -> None:
        self.manager = EthManager()

    @run_handler
    def start(self) -> None:
        block_number = self.manager.get_block_number()
        logger.info(f"block_number: {block_number.get_number()}")
        rpc_block = self.manager.get_block_by_number(block_number.number)
        try:
            last_block = LastBlock.objects.get(id=1)
        except LastBlock.DoesNotExist:
            last_block = LastBlock.objects.create(number=rpc_block.get_number(), hash=rpc_block.hash)

        if last_block.number < rpc_block.get_number():
            next_number = last_block.number + 1
            rpc_block = self.manager.get_block_by_number(Web3.toHex(next_number))
            block = self.insert_block(rpc_block)
            self.insert_transactions(block, rpc_block.transactions)

        last_block.number = rpc_block.get_number()
        last_block.hash = rpc_block.hash
        last_block.save()

    def insert_block(self, rpc_block):
        try:
            block = Blocks.objects.get(number=rpc_block.get_number())
        except Blocks.DoesNotExist:
            block = Blocks.create_with(rpc_block)
        return block

    def insert_transactions(self, block, transactions):
        for transaction in transactions:
            print(f"tx hash: {transaction.hash}")
            rpc_transaction = self.manager.get_transaction_by_hash(transaction.hash)
            try:
                transaction = Transactions.objects.get(hash=rpc_transaction.hash)
            except Transactions.DoesNotExist:
                transaction = Transactions.create_with(block, rpc_transaction)
            self.insert_receipt(transaction)

    def insert_receipt(self, transaction):
        rpc_receipt = self.manager.get_transaction_receipt(transaction.hash)
        try:
            receipt = Receipt.objects.get(transaction=transaction)
        except Receipt.DoesNotExist:
            receipt = Receipt.create_with(transaction, rpc_receipt)


check_block = CheckBlock()
check_block.start()
