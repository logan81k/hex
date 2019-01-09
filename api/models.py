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
    transactions_root = models.CharField(max_length=255, null=False)
    updated_time = models.DateTimeField(auto_now=True)
    created_time = models.DateTimeField(auto_now_add=True, editable=False)

    @classmethod
    def create_with_block(cls, b):
        return cls.objects.create(number=b.get_number(), hash=b.hash, parent_hash=b.parent_hash, nonce=b.nonce,
                                  size=b.get_size(), difficulty=b.get_difficulty(),
                                  total_difficulty=b.get_total_difficulty(), gas_limit=b.get_gas_limit(),
                                  gas_used=b.get_gas_used(), author=b.author, miner=b.miner,
                                  extra_data=b.extra_data, logs_bloom=b.logs_bloom, mix_hash=b.mix_hash,
                                  receipts_root=b.receipts_root, seal_fields=b.seal_fields, sha3_uncles=b.sha3_uncles,
                                  state_root=b.state_root, timestamp=b.get_timestamp(),
                                  transactions_root=b.transactions_root)


class Transactions(models.Model):
    block = models.ForeignKey(Blocks, on_delete=models.CASCADE)
    hash = models.CharField(max_length=255, null=False, unique=True)
    from_address = models.CharField(max_length=255, null=False)
    to_address = models.CharField(max_length=255, null=False)
    value = models.CharField(max_length=32, null=False)
    nonce = models.IntegerField(null=False)
    gas = models.IntegerField(null=False)
    gas_price = models.DecimalField(max_digits=36, decimal_places=18, null=False)
    input = models.TextField(max_length=255, null=False)
    chain_id = models.CharField(max_length=4, null=True)
    condition = models.CharField(max_length=255, null=True)
    creates = models.CharField(max_length=255, null=True)
    public_key = models.CharField(max_length=1024, null=False)
    raw = models.TextField(max_length=2048, null=False)
    transaction_index = models.CharField(max_length=4, null=False)
    standard_v = models.CharField(max_length=4, null=False)
    r = models.CharField(max_length=255, null=False)
    v = models.CharField(max_length=8, null=False)
    s = models.CharField(max_length=4096, null=False)

    @classmethod
    def create_with_transaction(cls, block, tx):
        return cls.objects.create(block=block, hash=tx.hash, from_address=tx.from_address, to_address=tx.to_address,
                                  value=tx.value, nonce=tx.get_nonce(), gas=tx.get_gas(), gas_price=tx.get_gas_price(),
                                  input=tx.input, chain_id=tx.chain_id, condition=tx.condition, creates=tx.creates,
                                  public_key=tx.public_key, raw=tx.raw, transaction_index=tx.transaction_index,
                                  standard_v=tx.standard_v, r=tx.r, v=tx.v, s=tx.s)
