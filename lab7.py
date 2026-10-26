import csv
import json
import re
from pathlib import Path


def load_drama_rows():
    candidates = [
        Path("kdramaMini.txt"),
        Path("kdrama.csv"),
        Path("kdrama (1).htm"),
    ]

    for path in candidates:
        if not path.exists():
            continue

        if path.suffix.lower() in {".htm", ".html"}:
            text = path.read_text(encoding="utf-8")
            match = re.search(
                r'<script type="application/json" data-target="react-app\.embeddedData">(.*?)</script>',
                text,
                re.DOTALL,
            )
            if match:
                payload = json.loads(match.group(1))
                rows = payload.get("payload", {}).get("codeViewBlobRoute", {}).get("csv", [])
                if rows:
                    return rows
            continue

        with open(path, newline="", encoding="utf-8") as file:
            rows = list(csv.reader(file))
            if rows:
                return rows

    raise FileNotFoundError(
        "No dataset file found. Expected kdramaMini.txt, kdrama.csv, or kdrama (1).htm"
    )


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

d = Hashtable(1009)

rows = load_drama_rows()

header = rows[0]
for row in rows[1:]:
    if len(row) < 8:
        continue

    name = row[0]
    rating = row[1]
    actor = row[2]
    year = row[7]

    drama = Drama(name, rating, actor, year)
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