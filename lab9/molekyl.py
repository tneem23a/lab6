from LinkedQ import LinkedQueue


class Syntaxfel(Exception):
    pass


ATOMER = """
H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr
Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd
Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er
Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th
Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs Mt Ds Rg Cn
Fl Lv
""".split()


def resten(q):
    return str(q)


def readFormel(q):
    readMol(q)

    if not q.isEmpty():
        raise Syntaxfel(
            "Felaktig gruppstart vid radslutet " + resten(q)
        )


def readMol(q):
    readGroup(q)

    while not q.isEmpty() and q.peek() != ")":
        readGroup(q)


def readGroup(q):

    if q.isEmpty():
        raise Syntaxfel(
            "Felaktig gruppstart vid radslutet "
        )

    if q.peek() == "(":

        q.dequeue()

        readMol(q)

        if q.isEmpty() or q.peek() != ")":
            raise Syntaxfel(
                "Saknad högerparentes vid radslutet " +
                resten(q)
            )

        q.dequeue()

        readNum(q)

    else:

        readAtom(q)

        if not q.isEmpty() and q.peek().isdigit():
            readNum(q)


def readAtom(q):

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