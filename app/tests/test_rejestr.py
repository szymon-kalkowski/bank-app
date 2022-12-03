import unittest
from ..Konto import Konto
from ..RejestrKont import RejestrKont

class TestRejestr(unittest.TestCase):
    imie = "Szymon"
    nazwisko = "Kalkowski"
    pesel = "02220604718"
    dane = {
        "imie": "Mateusz",
        "saldo": 20
    }
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

    def test_3_wyszukiwanie_konta_ktore_istnieje(self):
        konto = Konto(self.imie, self.nazwisko, "22222222222")
        RejestrKont.dodaj_konto(konto)
        wynik = RejestrKont.wyszukaj_konto_z_peselem("22222222222")
        self.assertEqual(wynik, konto)

    def test_4_wyszukiwanie_konta_ktore_nie_istnieje(self):
        wynik = RejestrKont.wyszukaj_konto_z_peselem("12345678901")
        self.assertEqual(wynik, None)

    def test_5_aktualizacja_konta_ktore_istnieje(self):
        konto = Konto(self.imie, self.nazwisko, "66666666666")
        RejestrKont.dodaj_konto(konto)
        aktualizacja = RejestrKont.zaktualizuj_konto_z_peselem("66666666666", self.dane)
        self.assertEqual(aktualizacja.imie, self.dane["imie"])
        self.assertEqual(aktualizacja.nazwisko, self.nazwisko)
        self.assertEqual(aktualizacja.pesel, "66666666666")
        self.assertEqual(aktualizacja.saldo, self.dane["saldo"])

    def test_6_usuwanie_konta_ktore_istnieje(self):
        konto = Konto(self.imie, self.nazwisko, "99999999999")
        RejestrKont.dodaj_konto(konto)
        ilosc_kont = RejestrKont.ile_kont()
        RejestrKont.usun_konto_z_peselem("99999999999")
        ilosc_kont_po = RejestrKont.ile_kont()
        self.assertEqual(ilosc_kont_po + 1, ilosc_kont)

    @classmethod
    def tearDownClass(cls):
        RejestrKont.lista = []