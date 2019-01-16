from web3 import Web3


class BlockNumber:
    def __init__(self, number) -> None:
        self.number = number

    def get_number(self):
        return Web3.toInt(hexstr=self.number)


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
        self.transactions = [Transaction(transaction) for transaction in block["transactions"]]
        self.transactions_root = block["transactionsRoot"]
        self.uncles = block["uncles"]

    def get_number(self):
        return Web3.toInt(hexstr=self.number)

    def get_gas_limit(self):
        return Web3.toInt(hexstr=self.gas_limit)

    def get_gas_used(self):
        return Web3.toInt(hexstr=self.gas_used)

    def get_size(self):
        return Web3.toInt(hexstr=self.size)

    def get_difficulty(self):
        return Web3.toInt(hexstr=self.difficulty)

    def get_total_difficulty(self):
        return Web3.toInt(hexstr=self.total_difficulty)

    def get_timestamp(self):
        ts = Web3.toInt(hexstr=self.timestamp)
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

    def get_block_number(self):
        return Web3.toInt(hexstr=self.block_number)

    def get_gas(self):
        return Web3.toInt(hexstr=self.gas)

    def get_gas_price(self):
        return Web3.toInt(hexstr=self.gas_price)

    def get_nonce(self):
        return Web3.toInt(hexstr=self.nonce)

    def get_transaction_index(self):
        return Web3.toInt(hexstr=self.transaction_index)

    def get_value(self):
        return Web3.toInt(hexstr=self.value)

    def get_ether_value(self):
        return Web3.fromWei(Web3.toInt(hexstr=self.value), 'ether')

    def get_nonce(self):
        return Web3.toInt(hexstr=self.nonce)


class Receipt:

    def __init__(self, receipt) -> None:
        self.block_hash = receipt['blockHash']
        self.block_number = receipt['blockNumber']
        self.contract_address = receipt['contractAddress']
        self.cumulative_gas_used = receipt['cumulativeGasUsed']
        self.from_address = receipt['from']
        self.gas_used = receipt['gasUsed']
        self.logs = receipt['logs']
        self.logs_bloom = receipt['logsBloom']
        self.root = receipt['root']
        self.status = receipt['status']
        self.to_address = receipt['to']
        self.transaction_hash = receipt['transactionHash']
        self.transaction_index = receipt['transactionIndex']

    def get_block_number(self):
        return int(self.block_number, 16)

    def get_gas_used(self):
        return int(self.gas_used, 16)

    def get_cumulative_gas_used(self):
        return int(self.cumulative_gas_used, 16)

    def get_transaction_index(self):
        return int(self.transaction_index, 16)

    def get_status(self):
        return int(self.status, 16)
