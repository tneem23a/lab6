from linkedQ import LinkedQueue


class Syntaxfel(Exception):
    pass


def readformel(q):

    readgroup(q)


def readgroup(q):

    readatom(q)
    readnum(q)


def readatom(q):

    readLETTER(q)

    if not q.isEmpty() and q.peek().islower():
        q.dequeue()


def readLETTER(q):

    if q.isEmpty():
        raise Syntaxfel("Saknad stor bokstav vid radslutet ")

    tecken = q.peek()

    if not tecken.isupper():
        raise Syntaxfel(
            "Saknad stor bokstav vid radslutet " + str(q)
        )

    q.dequeue()


def readnum(q):

    if q.isEmpty():
        return

    if not q.peek().isdigit():
        return

    tal = ""

    while not q.isEmpty() and q.peek().isdigit():
        tal += q.dequeue()

    if tal[0] == "0":
        raise Syntaxfel(
            "För litet tal vid radslutet " + tal[1:]
        )

    if int(tal) < 2:
        raise Syntaxfel(
            "För litet tal vid radslutet "
        )


while True:

    rad = input().strip()

    if rad == "#":
        break

    q = LinkedQueue()

    for tecken in rad:
        q.enqueue(tecken)

    try:
        readformel(q)
        print("Formeln är syntaktiskt korrekt")

    except Syntaxfel as fel:
        print(fel)