class HashNode:

    def __init__(self, key="", data=None):
        self.key = key
        self.data = data


class Hashtable:

    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def store(self, key, data):

        index = self.hashfunction(key)

        for node in self.table[index]:
            if node.key == key:
                node.data = data
                return

        self.table[index].append(HashNode(key, data))

    def search(self, key):

        index = self.hashfunction(key)

        for node in self.table[index]:
            if node.key == key:
                return node.data

        raise KeyError

    def hashfunction(self, key):

        h = 0

        for char in key:
            h = (h * 31 + ord(char)) % self.size

        return h

    def __getitem__(self, key):
        return self.search(key)

    def __contains__(self, key):

        index = self.hashfunction(key)

        for node in self.table[index]:
            if node.key == key:
                return True

        return False