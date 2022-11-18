import unittest
from ..Konto import Konto

class TestKredyt(unittest.TestCase):
    def testKredytUdzielony(self):
        konto_spelniajace_warunki = Konto("Szymon", "Kalkowski", "02220604718")
        konto_spelniajace_warunki.historia = [-100, 100, 100, 100, 600]
        czy_przyznany = konto_spelniajace_warunki.zaciagnij_kredyt(500)
        self.assertTrue(czy_przyznany, "Kredyt powienien zostać przyznany!")
        self.assertEqual(konto_spelniajace_warunki.saldo, 500, "Kredyt nie został przyznany poprawnie!")

    def testKredytNieudzielony3ostatnie(self):
        konto_3_ostatnie_nie_spelaniaja = Konto("Maciej", "Słupianek", "02250604716")
        konto_3_ostatnie_nie_spelaniaja.historia = [100, 100, 300, 250, -100, 300]
        czy_przyznany = konto_3_ostatnie_nie_spelaniaja.zaciagnij_kredyt(200)
        self.assertFalse(czy_przyznany, "Kredyt nie powinien zostać przyznany!")
        self.assertEqual(konto_3_ostatnie_nie_spelaniaja.saldo, 0, "Kredyt nie został przyznany poprawnie!")

    def testKredytNieudzielony5ostatnich(self):
        konto_5_ostatnich_nie_spelnia = Konto("Jan", "Kowalski", "03330604718")
        konto_5_ostatnich_nie_spelnia.historia = [100, -1000, -2000, 200, 500, 300]
        czy_przyznany = konto_5_ostatnich_nie_spelnia.zaciagnij_kredyt(300)
        self.assertFalse(czy_przyznany, "Kredyt nie powinien zostać przyznany!")
        self.assertEqual(konto_5_ostatnich_nie_spelnia.saldo, 0, "Kredyt nie został przyznany poprwanie!")

    def testKredytZaMaloTransakcji(self):
        konto_za_malo_transacji = Konto("Adam", "Nowak", "02256604718")
        konto_za_malo_transacji.historia = [100, 300, 400]
        czy_przyznany = konto_za_malo_transacji.zaciagnij_kredyt(200)
        self.assertFalse(czy_przyznany, "Kredyt nie powinien zostać przyznany!")
        self.assertEqual(konto_za_malo_transacji.saldo, 0, "Kredyt nie został przyznany prawidłowo!")