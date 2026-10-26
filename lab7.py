import csv

class DictHash:
    def __init__(self):
        self.table = {}

    def store(self, key, data):
        self.table[key] = data

    def search(self, key):
        if key in self.table:
            return self.table[key]
        raise KeyError

    def __getitem__(self, key):
        return self.search(key)

    def __contains__(self, key):
        return key in self.table

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
        bucket = self.table[index]


        for node in bucket:
            if node.key == key:
                node.data = data
                return


        bucket.append(HashNode(key, data))

    def search(self, key):


        index = self.hashfunction(key)
        bucket = self.table[index]

        for node in bucket:
            if node.key == key:
                return node.data

        raise KeyError

    def hashfunction(self, key):

        hashvalue = 0

        for tecken in key:
            hashvalue = (hashvalue * 31 + ord(tecken)) % self.size

        return hashvalue

    def __getitem__(self, key):
        return self.search(key)

    def __contains__(self, key):
        index = self.hashfunction(key)

        for node in self.table[index]:
            if node.key == key:
                return True

        return False

class Drama:
    def __init__(self, name, rating, actor, year):
        self.name = name
        self.rating = rating
        self.actor = actor
        self.year = year

    def __str__(self):
        return f"{self.name} ({self.year}), rating: {self.rating}"

d = DictHash()

with open("kdramaMini.txt", encoding="utf-8") as file:
    reader = csv.reader(file)

    next(reader)  # första rubriken
    next(reader)  # andra rubriken

    for row in reader:
        name = row[0]
        rating = row[1]
        actor = row[2]
        year = row[7]

        drama = Drama(name, rating, actor, year)

        # namnet används som key
        d.store(name, drama)


# Testa sökning
try:
    drama = d.search("Legend of the Blue Sea")
    print(drama)

except KeyError:
    print("Finns inte")


# Testa ett drama som inte finns
try:
    drama = d.search("Harry Potter")
    print(drama)

except KeyError:
    print("Finns inte")