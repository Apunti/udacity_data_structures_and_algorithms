import sys


class Huffman_Coding:

    def __init__(self, data, boolean=True):
        if not type(data) is str:
            print("Data must be a string!")
            return
        if len(data) == 0:
            print("Data can't be an empty string!")
            return
        self.tree = Tree()
        self.dic = {}
        self.encoding_dic = {}
        self.decoding_dic = {}
        if boolean:
            for char in data:
                if char in self.dic:
                    self.dic[char] += 1
                else:
                    self.dic[char] = 1
            self.priority_queue = Priority_Queue()
            for char in self.dic:
                node = Node(char, self.dic[char])
                self.priority_queue.add_node(node)

    def create_tree(self):
        if len(self.priority_queue.list) == 1:
            self.tree.root = Node(None, self.priority_queue.list[0].freq)
            self.tree.root.left = self.priority_queue.list[0]
            return
        while len(self.priority_queue.list) > 1:
            self.priority_queue.merge()
        self.tree.root = self.priority_queue.list[0]

    def create_encoding_dic(self):
        self._create_encoding_dic(self.tree.root, '')

    def _create_encoding_dic(self, current_node, number):
        if current_node.right is None and current_node.left is None:
            self.encoding_dic[current_node.value] = number
        elif current_node.right is None and current_node.left is not None:
            self._create_encoding_dic(current_node.left, number + '0')
        elif current_node.left is None and current_node.right is not None:
            self._create_encoding_dic(current_node.right, number + '1')
        else:
            self._create_encoding_dic(current_node.right, number + '1')
            self._create_encoding_dic(current_node.left, number + '0')

    def create_decoding_dic(self):
        if len(self.encoding_dic) == 0:
            return "first use create_encoding_dic method"
        for key in self.encoding_dic:
            self.decoding_dic[self.encoding_dic[key]] = key

    def encode_message(self, message):
        if len(self.encoding_dic) == 0:
            return "there's no encoding_dic"

        encoded_message = ''
        for char in message:
            encoded_message += self.encoding_dic[char]

        return encoded_message

    def decode_message(self, message):

        if len(self.decoding_dic) == 0:
            return "there's no decoding_dic"

        decoded_message = ''
        string = ''
        for char in message:
            word, string = self.find_codes(string + char)
            if word is not None:
                decoded_message += word
        return decoded_message

    def find_codes(self, string):
        if string in self.decoding_dic:
            return self.decoding_dic[string], ''
        else:
            return None, string


class Node:

    def __init__(self, value, freq):
        self.value = value
        self.freq = freq
        self.right = None
        self.left = None


class Tree:

    def __init__(self):
        self.root = Node(None, None)


class Priority_Queue:

    def __init__(self):
        self.list = []
        self.length = 0

    def merge(self):
        node1, node2 = self.list[0], self.list[1]
        new_node = Node(None, node1.freq + node2.freq)
        new_node.right = node1
        new_node.left = node2
        if len(self.list) == 2:
            self.list = [new_node]
            return
        self.list = self.list[2:]
        self.length -= 1
        for i in range(len(self.list)):
            if self.list[i].freq > new_node.freq:
                self.list.insert(i, new_node)
                return
        self.list.append(new_node)

    def add_node(self, node):
        length = len(self.list)
        if length == 0:
            self.list = [node]
            self.length += 1
        else:
            for i in range(length):
                if self.list[i].freq > node.freq:
                    if i == 0:
                        self.list = [node] + self.list
                        return
                    else:
                        self.list.insert(i, node)
                        return
            self.list.append(node)
            self.length += 1


def huffman_encoding(data):
    if not type(data) is str:
        print("Data must be a string!")
        return None, None
    if len(data) == 0:
        print("Data can't be an empty string!")
        return None, None

    huffman = Huffman_Coding(data)
    huffman.create_tree()
    huffman.create_encoding_dic()
    return huffman.encode_message(data), huffman.tree


def huffman_decoding(data, tree):
    huffman = Huffman_Coding(data, False)
    huffman.tree = tree
    huffman.create_encoding_dic()
    huffman.create_decoding_dic()
    return huffman.decode_message(data)


a_great_sentence = "The bird is the word"

print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
# "The size of the data is: 69"

encoded_data, output_tree = huffman_encoding(a_great_sentence)

print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
# "The size of the encoded data is: 36"
print("The content of the encoded data is: {}\n".format(encoded_data))
# 'The content of the encoded data is: 1001000100000011000111110101001111011100101100001000000101010100110101'

decoded_data = huffman_decoding(encoded_data, output_tree)

print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
# "The size of the decoded data is: 69"
print("The content of the encoded data is: {}\n".format(decoded_data))
# "The content of the encoded data is: The bird is the word"

empty_sentence = ''
_, _ = huffman_encoding(empty_sentence)
# "Data can't be an empty string!"

int_sentence = 2
_, _ = huffman_encoding(int_sentence)
# "Data must be a string!"

a_sentence = 'aaaaaa'
encoded_data, _ = huffman_encoding(a_sentence)
print(encoded_data)
# 000000
