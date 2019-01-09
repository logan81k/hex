import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hex.settings")
import django

django.setup()

import logging
from eth.managers.manager import EthManager
from api.models import LastBlock, Blocks, Transactions

logger = logging.getLogger(__name__)


class CheckBlock:

    def __init__(self) -> None:
        self.manager = EthManager()

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
            rpc_block = self.manager.get_block_by_number(hex(next_number))

        block = self.insert_block(rpc_block)
        self.insert_transactions(block, rpc_block.transactions)

    def insert_block(self, rpc_block):
        try:
            block = Blocks.objects.get(number=rpc_block.get_number())
        except Blocks.DoesNotExist:
            block = Blocks.create_with_block(rpc_block)
        return block

    def insert_transactions(self, block, transactions):
        for transaction in transactions:
            print(f"tx hash: {transaction.hash}")
            try:
                tx = Transactions.objects.get(hash=transaction.hash)
            except Transactions.DoesNotExist:
                tx = Transactions.create_with_transaction(block, transaction)



check_block = CheckBlock()
check_block.start()
