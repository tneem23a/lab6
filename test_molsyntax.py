import unittest
from linkedQ import LinkedQueue
from molsyntax import readLETTER
from molsyntax import Syntaxfel
from molsyntax import readatom
from molsyntax import readnum
from molsyntax import readformel

class TestMolsyntax(unittest.TestCase):

    def test_stor_bokstav(self):

        q = LinkedQueue()

        q.enqueue("A")

        try:
            readLETTER(q)
        except Syntaxfel:
            self.fail()

    def test_liten_bokstav(self):

        q = LinkedQueue()

        q.enqueue("a")

        with self.assertRaises(Syntaxfel):
            readLETTER(q)

def test_atom_en_bokstav(self):
    q = LinkedQueue()

    q.enqueue("H")

    try:
        readatom(q)
    except Syntaxfel:
        self.fail()


def test_atom_tva_bokstaver(self):

    q = LinkedQueue()

    q.enqueue("F")
    q.enqueue("e")

    try:
        readatom(q)
    except Syntaxfel:
        self.fail()

def test_nummer_godkant(self):

    q = LinkedQueue()

    q.enqueue("1")
    q.enqueue("2")

    try:
        readnum(q)
    except Syntaxfel:
        self.fail()


def test_nummer_noll(self):

    q = LinkedQueue()

    q.enqueue("0")

    with self.assertRaises(Syntaxfel):
        readnum(q)


def test_nummer_ett(self):

    q = LinkedQueue()

    q.enqueue("1")

    with self.assertRaises(Syntaxfel):
        readnum(q)

def test_formel(self):

    q = LinkedQueue()

    q.enqueue("F")
    q.enqueue("e")
    q.enqueue("1")
    q.enqueue("2")

    try:
        readformel(q)
    except Syntaxfel:
        self.fail()


if __name__ == "__main__":
    unittest.main()