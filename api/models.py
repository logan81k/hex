from decimal import Decimal

from django.db import models
# Create your models here.
from web3 import Web3


class LastBlock(models.Model):
    number = models.IntegerField(null=False)
    hash = models.CharField(max_length=255, null=False)
    updated_time = models.DateTimeField(auto_now=True)
    created_time = models.DateTimeField(auto_now_add=True, editable=False)


class Blocks(models.Model):
    number = models.IntegerField(null=False, unique=True)
    hash = models.CharField(max_length=255, null=False, unique=True)
    parent_hash = models.CharField(max_length=255, null=False, unique=True)
    nonce = models.CharField(max_length=255, null=False)
    size = models.IntegerField(null=False)
    difficulty = models.BigIntegerField(null=False)
    total_difficulty = models.CharField(max_length=255, null=False)
    gas_limit = models.IntegerField(null=False)
    gas_used = models.IntegerField(null=False)
    author = models.CharField(max_length=255, null=False)
    miner = models.CharField(max_length=128, null=False)
    extra_data = models.CharField(max_length=1024)
    logs_bloom = models.CharField(max_length=2048, null=False)
    mix_hash = models.CharField(max_length=255, null=False)
    receipts_root = models.CharField(max_length=255, null=False)
    seal_fields = models.CharField(max_length=1024, null=False)
    sha3_uncles = models.CharField(max_length=255, null=False)
    state_root = models.CharField(max_length=255, null=False)
    timestamp = models.DateTimeField(null=False)
    transactions_root = models.CharField(max_length=255, null=False)
    updated_time = models.DateTimeField(auto_now=True)
    created_time = models.DateTimeField(auto_now_add=True, editable=False)

    @classmethod
    def create_with(cls, b):
        return cls.objects.create(number=b.get_number(), hash=b.hash, parent_hash=b.parent_hash,
                                  nonce=b.nonce,
                                  size=b.get_size(), difficulty=b.get_difficulty(),
                                  total_difficulty=b.get_total_difficulty(),
                                  gas_limit=b.get_gas_limit(), gas_used=b.get_gas_used(), author=b.author,
                                  miner=b.miner,
                                  extra_data=b.extra_data, logs_bloom=b.logs_bloom,
                                  mix_hash=b.mix_hash, receipts_root=b.receipts_root,
                                  seal_fields=b.seal_fields, sha3_uncles=b.sha3_uncles,
                                  state_root=b.state_root, timestamp=b.get_timestamp(),
                                  transactions_root=b.transactions_root)


class Transactions(models.Model):
    block = models.ForeignKey(Blocks, on_delete=models.CASCADE)
    block_hash = models.CharField(max_length=255, null=False)
    block_number = models.IntegerField(null=False)
    chain_id = models.CharField(max_length=4, null=True)
    condition = models.CharField(max_length=255, null=True)
    creates = models.CharField(max_length=255, null=True)
    from_address = models.CharField(max_length=255, null=False)
    gas = models.CharField(max_length=255, null=False)
    gas_price = models.CharField(max_length=255, null=False)
    hash = models.CharField(max_length=255, null=False)
    input = models.TextField(null=False)
    nonce = models.IntegerField(null=False)
    public_key = models.CharField(max_length=1024, null=False)
    r = models.CharField(max_length=255, null=False)
    raw = models.TextField(null=False)
    s = models.TextField(null=False)
    to_address = models.CharField(max_length=255, null=True)
    value = models.DecimalField(max_digits=36, decimal_places=18, null=False)
    transaction_index = models.IntegerField(null=False)
    standard_v = models.CharField(max_length=4, null=False)
    v = models.CharField(max_length=8, null=False)

    @classmethod
    def create_with(cls, block, tx):
        return cls.objects.create(block=block, block_number=tx.get_block_number(),
                                  block_hash=tx.block_hash,
                                  from_address=tx.from_address, to_address=tx.to_address, hash=tx.hash,
                                  value=tx.get_ether_value(), nonce=tx.get_nonce(), gas=tx.get_gas(),
                                  gas_price=tx.get_gas_price(),
                                  input=tx.input, chain_id=tx.chain_id, condition=tx.condition, creates=tx.creates,
                                  public_key=tx.public_key, raw=tx.raw, transaction_index=tx.get_transaction_index(),
                                  standard_v=tx.standard_v, r=tx.r, v=tx.v, s=tx.s)


class Receipt(models.Model):
    transaction = models.ForeignKey(Transactions, on_delete=models.CASCADE)
    # block_hash = models.CharField(max_length=255, null=False)
    # block_number = models.IntegerField(null=False)
    contract_address = models.CharField(max_length=255, null=True)
    cumulative_gas_used = models.IntegerField(null=False)
    from_address = models.CharField(max_length=255, null=False)
    gas_used = models.IntegerField(null=False)
    logs = models.TextField(null=False)
    logs_bloom = models.TextField(null=False)
    root = models.CharField(max_length=255, null=True)
    status = models.IntegerField(null=False)
    to_address = models.CharField(max_length=255, null=True)
    transaction_hash = models.CharField(max_length=255, null=False)
    transaction_index = models.IntegerField(null=False)

    @classmethod
    def create_with(cls, transaction, receipt):
        return cls.objects.create(transaction=transaction, contract_address=receipt.contract_address,
                                  cumulative_gas_used=receipt.get_cumulative_gas_used(),
                                  from_address=receipt.from_address, gas_used=receipt.get_gas_used(), logs=receipt.logs,
                                  logs_bloom=receipt.logs_bloom, root=receipt.root, status=receipt.get_status(),
                                  to_address=receipt.to_address, transaction_hash=receipt.transaction_hash,
                                  transaction_index=receipt.get_transaction_index())
