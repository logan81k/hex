
class BlockNumber:
    def __init__(self, hex_number) -> None:
        self.hex_number = hex_number
        self.number = int(hex_number, 16)


class Block:
    def __init__(self, block) -> None:
        self.number = block["number"]
        self.transactions = block["transactions"]
