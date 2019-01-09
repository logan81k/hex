from decimal import Decimal

from django.db import models


# Create your models here.
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
    difficulty = models.CharField(max_length=255, null=False)
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
    updated_time = models.DateTimeField(auto_now=True)
    created_time = models.DateTimeField(auto_now_add=True, editable=False)

    @classmethod
    def create_with_block(cls, block):
        return cls.objects.create(number=block.get_number(), hash=block.hash, parent_hash=block.parent_hash,
                                  nonce=block.nonce, size=block.get_size(), difficulty=block.get_difficulty(),
                                  total_difficulty=block.get_total_difficulty(), gas_limit=block.get_gas_limit(),
                                  gas_used=block.get_gas_used(), author=block.author, miner=block.miner,
                                  extra_data=block.extra_data, logs_bloom=block.logs_bloom,
                                  mix_hash=block.mix_hash, receipts_root=block.receipts_root,
                                  seal_fields=block.seal_fields, sha3_uncles=block.sha3_uncles,
                                  state_root=block.state_root, timestamp=block.get_timestamp())


# class Transactions(models.Model):
#     block_id = models.ForeignKey(Blocks, on_delete=models.CASCADE)
#     hash = models.CharField(max_length=255, null=False)
#     from_address = models.CharField(max_length=255, null=False)
#     to_address = models.CharField(max_length=255, null=False)
#     gas = models.DecimalField(max_digits=36, decimal_places=18, null=False)
#     gas_price = models.DecimalField(max_digits=36, decimal_places=18, null=False)
#     chain_id = models.CharField(max_length=4, null=False)
#     condition = models.CharField(max_length=255, null=True)
#     creates = models.CharField(max_length=255, null=True)
#     input = models.CharField(max_length=255, null=False)
#     nonce = models.IntegerField(null=False)
#     public_key = models.CharField(max_length=1024, null=False)
#     r = models.CharField(max_length=255, null=False)
#     raw = models.CharField(max_length=2048, null=False)
#     s = models.CharField(max_length=4096, null=False)
#     standard_v = models.CharField(max_length=4, null=False)
#     transaction_index = models.CharField(max_length=4, null=False)
#     v = models.CharField(max_length=8, null=False)
#     value = models.CharField(max_length=32, null=False)
