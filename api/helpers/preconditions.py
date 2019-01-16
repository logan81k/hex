from api.exceptions import BlockDoesNotExistException, TransactionDoesNotExistException
from api.models import Blocks, Transactions


def exist_blocks_by_number(number):
    try:
        block = Blocks.objects.get(number=number)
    except Blocks.DoesNotExist:
        raise BlockDoesNotExistException(number)
    return block


def exist_transactions_by_block_number(block_number):
    try:
        transactions = Transactions.objects.filter(block_number=block_number)
    except Transactions.DoesNotExist:
        raise TransactionDoesNotExistException(hash)
    return transactions


def exist_transaction_by_hash(hash):
    try:
        transaction = Transactions.objects.get(hash=hash)
    except Transactions.DoesNotExist:
        raise TransactionDoesNotExistException(hash)
    return transaction
