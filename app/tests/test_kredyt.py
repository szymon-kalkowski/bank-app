import unittest
from ..Konto import Konto
from parameterized import parameterized

class TestKredyt(unittest.TestCase):
    imie = "Szymon"
    nazwisko = "Kalkowski"
    pesel = "02220604718"

    def setUp(self):
        self.konto = Konto(self.imie, self.nazwisko, self.pesel)

    @parameterized.expand([
        ([-100, 100, 100, 100, 600], 500, True, 500),
        ([100, 100, 300, 250, -100, 300], 200, False, 0),
        ([100, -1000, -2000, 200, 500, 300], 300, False, 0),
        ([100, 300, 400], 200, False, 0)
    ])

    def testKredyt(self, historia, kwota, oczekiwany_wynik, oczekiwane_saldo):
        self.konto.historia = historia
        czy_przyznany = self.konto.zaciagnij_kredyt(kwota)
        self.assertEqual(czy_przyznany, oczekiwany_wynik)
        self.assertEqual(self.konto.saldo, oczekiwane_saldo, "Kredyt nie został przyznany poprawnie!")