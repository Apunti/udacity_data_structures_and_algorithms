import hashlib


class Block:

    def __init__(self, timestamp, data, previous_hash=None):
        if type(data) is not str:
            print('Data must be a string!')
            return
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)

    @staticmethod
    def calc_hash(data):
        sha = hashlib.sha256()

        hash_str = data.encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()


class Blockchain:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_node(self, block):
        if self.length == 0:
            self.head = Node(block, None)
            self.tail = self.head
            self.length += 1
        elif self.length == 1:
            self.tail = Node(block, self.head)
            self.tail.previous_hash = self.head.value.hash
            self.length += 1
        else:
            actual_tail = self.tail
            self.tail = Node(block, actual_tail)
            self.tail.previous_hash = actual_tail.value.hash
            self.length += 1

    def print_chain(self):
        string = ''
        current_node = self.tail
        if current_node is None:
            print('No block added yet!')
            return
        while current_node is not None:
            string += current_node.value.data + ' -> '
            current_node = current_node.previous
        print(string)


class Node:

    def __init__(self, block, previous):
        self.value = block
        self.previous = previous


block1 = Block('11:00 2/4/2019', 'We are at the first block')
block2 = Block('14:00 3/5/2019', 'We are at the second block')
block3 = Block('21:00 5/6/2019', 'We are at the third block')

blockchain = Blockchain()
blockchain.add_node(block1)
blockchain.add_node(block2)
blockchain.add_node(block3)
blockchain.print_chain()
# We are at the third block -> We are at the second block -> We are at the first block ->

print(blockchain.tail.previous_hash == blockchain.tail.previous.value.hash)
# True

badblock = Block('11:00 2/4/2019', 2, None)
# Data must be a string!

emptyblockchain = Blockchain()
emptyblockchain.print_chain()
# 'No block added yet!'
