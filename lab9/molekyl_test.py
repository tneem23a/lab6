import unittest
from LinkedQ import LinkedQueue
from molekyl import Syntaxfel, kontrollera, readFormel


class TestMolekyl(unittest.TestCase):

    def test_korrekta_formler(self):
        self.assertEqual(
            kontrollera("H2O"),
            "Formeln är syntaktiskt korrekt"
        )

        self.assertEqual(
            kontrollera("Na"),
            "Formeln är syntaktiskt korrekt"
        )

        self.assertEqual(
            kontrollera("Si(C3(COOH)2)4(H2O)7"),
            "Formeln är syntaktiskt korrekt"
        )

    def test_okand_atom(self):
        self.assertTrue(
            kontrollera("(Xx4)5").startswith("Okänd atom")
        )

    def test_for_litet_tal(self):
        self.assertTrue(
            kontrollera("H0").startswith("För litet tal")
        )

        self.assertTrue(
            kontrollera("H1C").startswith("För litet tal")
        )

    def test_saknad_hogerparentes(self):
        self.assertTrue(
            kontrollera("C(OH4C").startswith("Saknad högerparentes")
        )

    def test_saknad_stor_bokstav(self):
        self.assertTrue(
            kontrollera("Nacl").startswith("Saknad stor bokstav")
        )


if __name__ == "__main__":
    unittest.main()