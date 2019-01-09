import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hex.settings")
import django

django.setup()

import logging
from api.models import LastBlock, Blocks
from eth.clients.eth_client import EthClient
from eth.clients.eth_requester import EthRequester


logger = logging.getLogger(__name__)


def process_block(block):
    pass


def main(argv):
    requester = EthRequester("10.0.1.163", 8898)
    client = EthClient(requester)
    block_number = client.get_block_number()
    logger.info(f"block_number: {block_number.get_number()}")
    block = client.get_block_by_number(block_number.number)
    try:
        last_block = LastBlock.objects.get(id=1)
    except LastBlock.DoesNotExist:
        last_block = LastBlock.objects.create(number=block.get_number(), hash=block.hash)

    if last_block.number < block.get_number():
        print("gogogo")
        next_number = last_block.number + 1
        block = client.get_block_by_number(hex(next_number))
        try:
            next_block = Blocks.objects.get(number=block.get_number())
        except Blocks.DoesNotExist:
            print(block.get_difficulty())
            print(block.get_total_difficulty())
            next_block = Blocks.create_with_block(block)

        process_block(next_block)


        last_block.number = next_number
        last_block.save()


if __name__ == '__main__':
    main(sys.argv)
