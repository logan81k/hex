import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hex.settings")
import django

django.setup()

import logging
from eth.clients.eth_client import EthClient
from eth.clients.eth_requester import EthRequester

from eth.models import LastBlock, Blocks

logger = logging.getLogger(__name__)


def main(argv):
    requester = EthRequester("10.0.1.163", 8898)
    client = EthClient(requester)
    block_number = client.get_block_number()
    block_response = client.get_block_by_number(block_number.number)
    try:
        last_block = LastBlock.objects.get(id=1)
    except LastBlock.DoesNotExist:
        last_block = LastBlock.objects.create(number=block_response.number, hash=block_response.hash)

    if last_block.number < block_response.get_number():
        next_number = last_block.number + 1
        block_response = client.get_block_by_number(hex(next_number))
        try:
            next_block = Blocks.objects.get(number=block_response.get_number())
        except Blocks.DoesNotExist:
            next_block = Blocks.create_with_block(block_response)
        print(next_block)


if __name__ == '__main__':
    main(sys.argv)
