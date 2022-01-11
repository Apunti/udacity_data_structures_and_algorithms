from collections import OrderedDict


class LRU_Cache(object):

    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.cache:
            value = self.cache[key]
            del self.cache[key]
            self.cache[key] = value
            return value
        else:
            return -1

    def set(self, key, value):
        if self.capacity == 0:
            print("Can't perform operations on 0 capacity cache")
            return
        if key in self.cache:
            del self.cache[key]
            self.cache[key] = value
        else:
            if len(self.cache) == self.capacity:
                self.cache.popitem(False)
            self.cache[key] = value


### TEST CASES ###

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))
# 1
print(our_cache.get(2))
# 2
print(our_cache.get(9))
# -1

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))
# -1

new_cache = LRU_Cache(0)
new_cache.set(1, 1)
# "Can't perform operations on 0 capacity cache"
print(new_cache.get(1))
# should return -1

our_cache = LRU_Cache(2)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(1, 10)
print(our_cache.get(1))
# 10
print(our_cache.get(2))
# 2
