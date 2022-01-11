class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root
        for char in word:
            current_node = current_node.insert(char)
        current_node.is_word = True

    def find(self, prefix):
        current_node = self.root
        for char in prefix:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                print("Not Found")
                return
        return current_node


class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

    def insert(self, char):
        if char in self.children:
            pass
            # self.children[char]
        else:
            self.children[char] = TrieNode()
        return self.children[char]

    def suffixes(self, suffix='', suffix_list=None):
        if suffix_list is None:
            suffix_list = []

        if len(self.children) == 0:
            return suffix_list.append(suffix)
        else:
            for child in self.children:
                self.children[child].suffixes(suffix + child, suffix_list)
        return suffix_list


### TEST CASES ###

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for w in wordList:
    MyTrie.insert(w)

prefixNode1 = MyTrie.find("ant")
print(prefixNode1.suffixes())
# ['hology', 'agonist', 'onym']


prefixNode1 = MyTrie.find("")
print(prefixNode1.suffixes())
# ["ant", "anthology", "antagonist", "antonym","fun", "function", "factory",
# "trie", "trigger", "trigonometry", "tripod"]


prefixNode1 = MyTrie.find("hey")
# 'Not Found'
