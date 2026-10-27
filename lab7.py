from hashtable import Hashtable

import json
import re


def load_drama_rows():
    # Läs in HTML-filen som innehåller dramaseriernas data.
    with open("kdrama (1).htm", encoding="utf-8") as file:
        text = file.read()

    # Leta upp JSON-datan som är inbäddad i ett script-element i HTML-filen.
    match = re.search(
        r'<script type="application/json" data-target="react-app\.embeddedData">(.*?)</script>',
        text,
        re.DOTALL
    )

    # Omvandla den hittade JSON-texten till Python-data.
    payload = json.loads(match.group(1))

    # Hämta och returnera raderna med dramaseriernas information.
    return payload["payload"]["codeViewBlobRoute"]["csv"]


class Drama:
    # Representerar en dramaserie och dess egenskaper.
    def __init__(self, name, rating, actor, year):
        self.name = name
        self.rating = rating
        self.actor = actor
        self.year = year

    # Bestämmer hur en dramaserie visas som text.
    def __str__(self):
        return f"{self.name} ({self.year}), rating: {self.rating}"


# Skapa en hashtabell med plats för 1009 listor.
d = Hashtable(1009)

# Läs in alla rader från filen.
rows = load_drama_rows()

# Hoppa över den första raden, som innehåller kolumnrubrikerna.
for row in rows[1:]:

    # Hoppa över rader som saknar något av de fält vi behöver.
    if len(row) < 8:
        continue

    # Hämta namn, betyg, skådespelare och år från radens kolumner.
    name = row[0]
    rating = row[1]
    actor = row[2]
    year = row[7]

    # Skapa ett Drama-objekt för den aktuella raden.
    drama = Drama(name, rating, actor, year)

    # Spara objektet i hashtabellen med dramats namn som nyckel.
    d.store(name, drama)

# Hitta den längsta listan i tabellen.
# Listorna innehåller flera element när deras nycklar hamnar på samma plats.
max_krock = max(len(bucket) for bucket in d.table)
print("Största krocklista:", max_krock)

# Försök att hitta en serie med dess namn som nyckel.
try:
    drama = d.search("Legend of the Blue Sea")
    print(drama)

# Visa ett meddelande om nyckeln inte finns i hashtabellen.
except KeyError:
    print("Finns inte")

# Testa även att söka efter en titel som kanske inte finns i datan.
try:
    drama = d.search("Harry Potter")
    print(drama)

except KeyError:
    print("Finns inte")
