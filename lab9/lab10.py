from molgrafik import Ruta, Molgrafik
from hashtest import skapaAtomlista, lagraHashtabell



#atomtabell skapas en gång
atomlista = skapaAtomlista()
atomtabell = lagraHashtabell(atomlista)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedQ:
    def __init__(self):
        self.first = None
        self.last = None

    def isEmpty(self):
        return self.first is None

    def enqueue(self, value):
        node = Node(value)
        if self.isEmpty():
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node

    def dequeue(self):
        value = self.first.value
        self.first = self.first.next
        if self.first is None:
            self.last = None
        return value

    def peek(self):
        if self.isEmpty():
            return None
        return self.first.value


class Syntaxfel(Exception):
    pass


ATOMS = """
H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca
Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr
Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te
I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm
Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn
Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr
Rf Db Sg Bh Hs Mt Ds Rg Cn Fl Lv
""".split()


def read_LETTER(q):
    if q.isEmpty() or not q.peek().isupper():
        raise Syntaxfel("Saknad stor bokstav vid radslutet")

    return q.dequeue()


def read_letter(q):
    if not q.isEmpty() and q.peek().islower():
        return q.dequeue()
    return ""


def read_atom(q):
    atom = read_LETTER(q)
    atom += read_letter(q)

    if atom not in ATOMS:
        raise Syntaxfel("Okänd atom vid radslutet")

    return atom

def read_num(q):
    number = ""

    if q.peek() == "0":
        q.dequeue()
        raise Syntaxfel("För litet tal vid radslutet")

    while not q.isEmpty() and q.peek().isdigit():
        number += q.dequeue()

    if int(number) < 2:
        raise Syntaxfel("För litet tal vid radslutet")
    return int(number)


def readgroup(q):

    if q.isEmpty():
        raise Syntaxfel("Felaktig gruppstart vid radslutet")

    if q.peek() == "(": #programmet får en molekyl med en parantes + innehåll

        ruta = Ruta() #en ny ruta skapas

        q.dequeue() #vänstra parantesen läses bort

        ruta.down = readmol(q) #innehållet i parantesen läses med readmol
        #ruta.down sparar sedan resultatet
        #down pekar alltså på den första noden inuti parantesgruppen

        if q.isEmpty() or q.peek() != ")":
            raise Syntaxfel("Saknad högerparentes vid radslutet")

        q.dequeue()

        if q.isEmpty() or not q.peek().isdigit():
            raise Syntaxfel("Saknad siffra vid radslutet")

        ruta.num = read_num(q)

        return ruta

    elif q.peek().isupper():

        atom = read_atom(q)

        num = 1

        if not q.isEmpty() and q.peek().isdigit():
            num = read_num(q)

        return Ruta(atom, num)

    elif q.peek().islower():
        raise Syntaxfel("Saknad stor bokstav vid radslutet")

    else:
        raise Syntaxfel("Felaktig gruppstart vid radslutet")

def readmol(q):

    first = readgroup(q)
    current = first

    while not q.isEmpty() and q.peek() != ")":

        if not q.peek().isupper() and q.peek() != "(":
            raise Syntaxfel("Saknad stor bokstav vid radslutet")

        #en ny grupp läses
        ny = readgroup(q) #en ny nod ska skapas med den första gruppen

        current.next = ny #pekare, kopplar ihop den första noden,
                          # med parantesnoden
        current = ny #ska flytta current till den nya noden
        #alltså, next pekar på nästa atom/grupp i molekylen

    return first

def readformel(q):
    mol = readmol(q)

    if not q.isEmpty():
        raise Syntaxfel("Felaktig gruppstart vid radslutet")
    return mol


def weight(mol):

    if mol is None:
        return 0

    if mol.atom == "()": #om molekylen har en parantes dvs innehåll
        vikt = weight(mol.down) * mol.num#kommer denna beräkning att ske för att få vikten
    else: #om molekylen inte har en parantes tex som H2O,
        atom = atomtabell.search(mol.atom) #så kommer atomens vikt att sökas i atomtabellen ist
        vikt = atom.vikt * mol.num #och så sker denna beräkning ist för att få fram vikten

    return vikt + weight(mol.next) #rekursivt anrop till nästa nod
#basfallet: när molekylen tar slut blir mol.next == None
#--> då returnerar funktionen ist 0


def main():
    import sys

    for line in sys.stdin:
        line = line.strip()

        if line == "#":
            break

        if line == "":
            continue

        q = LinkedQ()

        for ch in line:
            q.enqueue(ch)

        try:
            mol = readformel(q)
            print("Formeln är syntaktiskt korrekt")

            print("Molekylvikt:", weight(mol))

            mg = Molgrafik()
            mg.show(mol)
            mg.root.mainloop()



        except Syntaxfel as e:
            rest = ""
            while not q.isEmpty():
                rest += q.dequeue()

            print(str(e) + " " + rest)


if __name__ == "__main__":
    main()