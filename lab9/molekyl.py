from LinkedQ import LinkedQueue


class Syntaxfel(Exception):
    """Undantag som används när en kemisk formel inte följer grammatiken."""


# Alla atomnamn som accepteras av parsern. Varje namn skrivs i
# det format som kan förekomma i en kemisk formel, till exempel "H" eller "Na".
ATOMER = """
H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr
Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd
Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er
Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th
Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs Mt Ds Rg Cn
Fl Lv
""".split()


def resten(q):
    #Returnerar den återstående delen av kön som text för felmeddelanden.
    return str(q)


def readFormel(q):
    #Tolkar en fullständig formel och accepterar bara exakt en giltig molekyl.
    readMol(q)

    if not q.isEmpty():
        raise Syntaxfel(
            "Felaktig gruppstart vid radslutet " + resten(q)
        )


def readMol(q):
    #Läser en eller flera grupper som följer varandra i en molekyl
    readGroup(q)

    while not q.isEmpty() and q.peek() != ")":
        readMol(q)


def readGroup(q):
    #Läser antingen en atomgrupp i parentes eller en ensam atom

    if q.isEmpty():
        raise Syntaxfel(
            "Felaktig gruppstart vid radslutet "
        )

    if q.peek() == "(":
        # En parentesindelad grupp börjar med "(" och måste avslutas med ")".
        q.dequeue()

        readMol(q)

        if q.isEmpty() or q.peek() != ")":
            raise Syntaxfel(
                "Saknad högerparentes vid radslutet " +
                resten(q)
            )

        q.dequeue()

        # Efter en avslutad grupp kan det finnas ett indexnummer, exempel H2 eller (OH)2.
        readNum(q)

    else:
        # Om det inte finns en inledande parentes så måste det vara en atom.
        readAtom(q)

        if not q.isEmpty() and q.peek().isdigit():
            readNum(q)


def readAtom(q):
    #Läser en atom, inklusive ett eventuellt litet bokstav i namnet

    if q.isEmpty() or not q.peek().isupper():
        raise Syntaxfel(
            "Saknad stor bokstav vid radslutet " +
            resten(q)
        )

    atom = q.dequeue()

    if not q.isEmpty() and q.peek().islower():
        atom += q.dequeue()

    if atom not in ATOMER:
        raise Syntaxfel(
            "Okänd atom vid radslutet " +
            resten(q)
        )


def readNum(q):
    #Läser ett siffertal efter en atom eller grupp och kräver minst 2

    if q.isEmpty() or not q.peek().isdigit():
        raise Syntaxfel(
            "Saknad siffra vid radslutet " +
            resten(q)
        )

    tal = ""

    while not q.isEmpty() and q.peek().isdigit():
        tal += q.dequeue()

    if int(tal) < 2:
        raise Syntaxfel(
            "För litet tal vid radslutet " +
            resten(q)
        )


def kontrollera(formel):
    #Kontrollerar en formel genom att skicka den till parsern

    q = LinkedQueue()

    for tecken in formel:
        q.enqueue(tecken)

    try:
        readFormel(q)
        return "Formeln är syntaktiskt korrekt"

    except Syntaxfel as fel:
        return str(fel)


if __name__ == "__main__":
    # Interaktiv konsolläggning: använd "#" för att avsluta programmet.
    while True:

        rad = input()

        if rad == "#":
            break

        q = LinkedQueue()

        for tecken in rad:
            q.enqueue(tecken)

        try:
            readFormel(q)
            print("Formeln är syntaktiskt korrekt")

        except Syntaxfel as fel:
            print(fel)