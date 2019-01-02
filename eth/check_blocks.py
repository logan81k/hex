import os
import sys

from eth.clients.eth_client import EthClient
from eth.clients.eth_requester import EthRequester

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hex.settings")
import django

django.setup()


def main(argv):
    requester = EthRequester("10.0.1.163", 8898)
    client = EthClient(requester)
    block_number = client.get_block_number()
    print(block_number.hex_number)
    print(block_number.number)

    block = client.get_block_by_number(block_number.number)
    print(block)
    # try:
    #     main = Main.objects.get(id=1)
    # except Main.DoesNotExist as e:
    #     main = Main.objects.create(number=block_number, hash=block_hash)
    #
    # if main.number < block_number:
    #     next_number = main.number + 1
    #     rpc_body = {"jsonrpc": "2.0", "method": "eth_getBlockByNumber", "params": [hex(next_number), True], "id": 100}


if __name__ == '__main__':
    main(sys.argv)
