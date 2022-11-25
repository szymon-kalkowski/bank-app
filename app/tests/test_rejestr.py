import unittest
from ..Konto import Konto
from ..RejestrKont import RejestrKont

class TestRejestr(unittest.TestCase):
    imie = "Szymon"
    nazwisko = "Kalkowski"
    pesel = "02220604718"
    @classmethod
    def setUpClass(cls):
        konto = Konto(cls.imie, cls.nazwisko, cls.pesel)
        RejestrKont.dodaj_konto(konto)

    def test_1_dodawanie_pierwszego_konta(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto1 = Konto("Adam", self.nazwisko, self.pesel)
        RejestrKont.dodaj_konto(konto)
        RejestrKont.dodaj_konto(konto1)
        self.assertEqual(RejestrKont.ile_kont(), 3, "Nieprawidłowa ilość kont.")

    def test_2_dodawanie_pierwszego_konta(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        RejestrKont.dodaj_konto(konto)
        self.assertEqual(RejestrKont.ile_kont(), 4, "Nieprawidłowa ilość kont.")

    @classmethod
    def tearDownClass(cls):
        RejestrKont.lista = []