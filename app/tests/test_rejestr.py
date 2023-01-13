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
        konto = Konto(self.imie, self.nazwisko, '02223334701')
        dodane_konto = RejestrKont.dodaj_konto(konto)
        self.assertEqual(RejestrKont.ile_kont(), 2, "Nieprawidłowa ilość kont.")
        self.assertEqual(dodane_konto, konto)

    def test_2_wyszukiwanie_konta_ktore_istnieje(self):
        konto = Konto(self.imie, self.nazwisko, "22222222222")
        dodane_konto = RejestrKont.dodaj_konto(konto)
        self.assertEqual(dodane_konto, konto)
        wynik = RejestrKont.wyszukaj_konto_z_peselem("22222222222")
        self.assertEqual(wynik, konto)

    def test_3_wyszukiwanie_konta_ktore_nie_istnieje(self):
        wynik = RejestrKont.wyszukaj_konto_z_peselem("12345678901")
        self.assertEqual(wynik, None)

    def test_4_aktualizacja_konta_ktore_istnieje(self):
        konto = Konto(self.imie, self.nazwisko, "66666666666")
        dodane_konto = RejestrKont.dodaj_konto(konto)
        self.assertEqual(dodane_konto, konto)
        aktualizacja = RejestrKont.zaktualizuj_konto_z_peselem("66666666666", self.dane)
        self.assertEqual(aktualizacja.imie, self.dane["imie"])
        self.assertEqual(aktualizacja.nazwisko, self.nazwisko)
        self.assertEqual(aktualizacja.pesel, "66666666666")
        self.assertEqual(aktualizacja.saldo, self.dane["saldo"])

    def test_5_usuwanie_konta_ktore_istnieje(self):
        konto = Konto(self.imie, self.nazwisko, "99999999999")
        RejestrKont.dodaj_konto(konto)
        ilosc_kont = RejestrKont.ile_kont()
        usuniete_konto = RejestrKont.usun_konto_z_peselem("99999999999")
        self.assertEqual(usuniete_konto, konto)
        ilosc_kont_po = RejestrKont.ile_kont()
        self.assertEqual(ilosc_kont_po + 1, ilosc_kont)
    
    def test_6_dodawanie_konta_ktore_istnieje(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        dodane_konto = RejestrKont.dodaj_konto(konto)
        ile_kont = RejestrKont.ile_kont()
        self.assertEqual(RejestrKont.ile_kont(), ile_kont, "Nieprawidłowa ilość kont.")
        self.assertEqual(dodane_konto, None)
        
    def test_7_usuwanie_konta_ktore_nie_istnieje(self):
        ile_kont = RejestrKont.ile_kont()
        usuniete_konto = RejestrKont.usun_konto_z_peselem('12359235710')
        ile_kont_po = RejestrKont.ile_kont()
        self.assertEqual(usuniete_konto, None)
        self.assertEqual(ile_kont_po, ile_kont)

    def test_8_usuwanie_wszystkich_kont(self):
        konto1 = Konto(self.imie, self.nazwisko, "38501573581")
        konto2 = Konto(self.imie, self.nazwisko, "38501673281")
        RejestrKont.dodaj_konto(konto1)
        RejestrKont.dodaj_konto(konto2)
        lista = RejestrKont.usun_wszystkie_konta()
        ile_kont = RejestrKont.ile_kont()
        self.assertEqual(len(lista), 0)
        self.assertEqual(ile_kont, 0)

    @classmethod
    def tearDownClass(cls):
        RejestrKont.lista = []