from hashtable import Hashtable

h = Hashtable(11)

h.store("KTH", "Stockholm")
h.store("SU", "Stockholm")

print(h.search("KTH"))
print(h.search("SU"))

try:
    print(h.search("UU"))
except KeyError:
    print("Finns inte")