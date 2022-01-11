class RouteTrie:
    def __init__(self, root_handler):
        self.root = RouteTrieNode(root_handler)

    def insert(self, path, handler):
        current_node = self.root
        for word in path:
            current_node = current_node.insert(word)
        current_node.handler = handler

    def find(self, path):
        current_node = self.root
        for word in path:
            if word in current_node.children:
                current_node = current_node.children[word]
            else:
                return None
        return current_node.handler


class RouteTrieNode:
    def __init__(self, handler):
        self.children = {}
        self.handler = handler

    def insert(self, word):
        if word in self.children:
            pass
            # self.children[word]
        else:
            self.children[word] = RouteTrieNode(None)
        return self.children[word]


class Router:
    def __init__(self, root_handler, not_found_handler):
        self.not_found_handler = not_found_handler
        self.routeTrie = RouteTrie(root_handler)

    def add_handler(self, path, handler):
        path = self.split_path(path)
        self.routeTrie.insert(path, handler)

    def lookup(self, path):
        path = self.split_path(path)
        current_node = self.routeTrie.root
        for word in path:
            if word in current_node.children:
                current_node = current_node.children[word]
            else:
                return self.not_found_handler
        if current_node.handler is None:
            return self.not_found_handler
        else:
            return current_node.handler

    @staticmethod
    def split_path(path):
        if len(path) == 0:
            return ['']
        if path[-1] == '/':
            return path.split('/')[1:-1]
        else:
            return path.split('/')[1:]


### TEST CASES ###

router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")

print(router.lookup("/"))
# 'root handler'

print(router.lookup("/home/about/"))
# 'about handler'

print(router.lookup("/home/about/me"))
# 'not found handler'

print(router.lookup(""))
# 'not found handler'
