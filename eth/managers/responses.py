from decimal import Decimal


class BlockNumber:
    def __init__(self, number) -> None:
        self.number = number

    def get_number(self):
        return int(self.number, 16)


class Block:
    def __init__(self, block) -> None:
        self.number = block["number"]
        self.hash = block["hash"]
        self.parent_hash = block["parentHash"]
        self.nonce = block["nonce"]
        self.size = block["size"]
        self.difficulty = block["difficulty"]
        self.total_difficulty = block["totalDifficulty"]
        self.gas_limit = block["gasLimit"]
        self.gas_used = block["gasUsed"]
        self.author = block["author"]
        self.miner = block["miner"]
        self.extra_data = block["extraData"]
        self.logs_bloom = block["logsBloom"]
        self.mix_hash = block["mixHash"]
        self.receipts_root = block["receiptsRoot"]
        self.seal_fields = block["sealFields"]
        self.sha3_uncles = block["sha3Uncles"]
        self.state_root = block["stateRoot"]
        self.timestamp = block["timestamp"]
        self.transactions = self._transactions(block["transactions"])
        self.transactions_root = block["transactionsRoot"]
        self.uncles = block["uncles"]

    def _transactions(self, transactions):
        return [Transaction(transaction) for transaction in transactions]

    def get_number(self):
        return int(self.number, 16)

    def get_gas_limit(self):
        return int(self.gas_limit, 16)

    def get_gas_used(self):
        return int(self.gas_used, 16)

    def get_size(self):
        return int(self.size, 16)

    def get_difficulty(self):
        return int(self.difficulty, 16)

    def get_total_difficulty(self):
        return int(self.total_difficulty, 16)

    def get_timestamp(self):
        ts = int(self.timestamp, 16)
        from django.utils.datetime_safe import datetime
        return datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')


class Transaction:
    def __init__(self, transaction) -> None:
        self.block_hash = transaction["blockHash"]
        self.block_number = transaction["blockNumber"]
        self.chain_id = transaction["chainId"]
        self.condition = transaction["condition"]
        self.creates = transaction["creates"]
        self.from_address = transaction["from"]
        self.gas = transaction["gas"]
        self.gas_price = transaction["gasPrice"]
        self.hash = transaction["hash"]
        self.input = transaction["input"]
        self.nonce = transaction["nonce"]
        self.public_key = transaction["publicKey"]
        self.r = transaction["r"]
        self.raw = transaction["raw"]
        self.s = transaction["s"]
        self.standard_v = transaction["standardV"]
        self.to_address = transaction["to"]
        self.transaction_index = transaction["transactionIndex"]
        self.v = transaction["v"]
        self.value = transaction["value"]

    def get_gas(self):
        return int(self.gas, 16)

    def get_gas_price(self):
        return int(self.gas_price, 16)

    def get_nonce(self):
        return int(self.nonce, 16)


