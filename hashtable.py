class HashNode:
    #Lagrar en nyckel och dess tillhörande data.

    def __init__(self, key="", data=None):
        self.key = key
        self.data = data


class Hashtable:
    #Hashtabell som hanterar kollisioner med kedjning.

    def __init__(self, size):
        self.size = size
        # Varje plats i tabellen innehåller en lista med noder.
        self.table = [[] for _ in range(size)]

    def store(self, key, data):
        #Lagra data för en nyckel, eller uppdatera befintliga data.
        index = self.hashfunction(key)

        # Om nyckeln redan finns uppdateras dess data.
        for node in self.table[index]:
            if node.key == key:
                node.data = data
                return

        # Annars läggs en ny nod till i listan på den beräknade platsen.
        self.table[index].append(HashNode(key, data))

    def search(self, key):
        #Hämta data för en nyckel.
        index = self.hashfunction(key)

        # Sök igenom listan eftersom flera nycklar kan hamna på samma plats.
        for node in self.table[index]:
            if node.key == key:
                return node.data

        #Nyckeln finns inte i tabellen.
        raise KeyError

    def hashfunction(self, key):
        #Beräkna vilken plats i tabellen en nyckel ska använda.
        h = 0

        # Bygg upp ett hashvärde tecken för tecken och håll det inom tabellens storlek.
        for char in key:
            h = (h * 31 + ord(char)) % self.size

        return h

    def __getitem__(self, key):
        # Gör det möjligt att hämta data med hakparenteser, till exempel table[key].
        return self.search(key)

    def __contains__(self, key):
        # Gör det möjligt att kontrollera medlemskap med "key in table".
        index = self.hashfunction(key)

        for node in self.table[index]:
            if node.key == key:
                return True

        return False
