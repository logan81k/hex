
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
        self.transactions = block["transactions"]
        self.uncles = block["uncles"]

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

