import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta_bez_kodu(self):
        pierwsze_konto = Konto("Dariusz", "Januszewski", "02220604718")
        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel, "02220604718")
        self.assertEqual(pierwsze_konto.kod, None, "Kod został podany a saldo pozostało zerowe.")

    def test_za_krotki_pesel(self):
        konto_za_krotki_pesel = Konto("Szymon", "Kalkowski", "01279746")
        self.assertEqual(konto_za_krotki_pesel.pesel, "Niepoprawny pesel!", "Pesel jest za krótki a nie ma błędu!")

    def test_za_dlugi_pesel(self):
        konto_za_dlugi_pesel = Konto("Szymon", "Kalkowski", "0127974613764183")
        self.assertEqual(konto_za_dlugi_pesel.pesel, "Niepoprawny pesel!", "Pesel jest za długi a nie ma błędu!")

    def test_poprawny_kod_rabatowy(self):
        konto_z_kodem = Konto("Marcin", "Dymek", "12345678912", "PROM_123")
        self.assertEqual(konto_z_kodem.kod, "PROM_123", "Kod rabatowy nie zosatał zapisany!")
        self.assertEqual(konto_z_kodem.saldo, 50, "Kod rabatowy niepoprawnie naliczony!")
    
    def test_niepoprawny_kod_rabatowy(self):
        konto_z_niepoprawnym_kodem = Konto("Maciej", "Słupianek", "12345678921", "PORM_123")
        self.assertEqual(konto_z_niepoprawnym_kodem.saldo, 0, "Zwiększono saldo mimo niepoprawnego kodu!")

    def test_kod_dla_mlodych(self):
        konto_z_kodem_dla_mlodych = Konto("Dawid", "Nider", "02220604718", "PROM_420")
        self.assertEqual(konto_z_kodem_dla_mlodych.rok_urodzenia(), 2002, "Nipoprawny rok urodzenia!")
        self.assertEqual(konto_z_kodem_dla_mlodych.urodzony_po_1960(), True, "Ten użytkownik urodził się po 1960!")
        self.assertEqual(konto_z_kodem_dla_mlodych.saldo, 50, "Nie naliczono bonusu mimo odpowiedniego wieku i kodu rabatowego!")

    def test_kod_dla_starych(self):
        konto_z_kodem_dla_starych = Konto("Maryla", "Rodowicz", "92811461823", "PROM_123")
        self.assertEqual(konto_z_kodem_dla_starych.rok_urodzenia(), 1892, "Niepoprawny rok urodzenia!")
        self.assertEqual(konto_z_kodem_dla_starych.urodzony_po_1960(), False, "Ten użytkownik urodził się przed 1960!")
        self.assertEqual(konto_z_kodem_dla_starych.saldo, 0, "Saldo powinno wynosić 0!")

    def test_niepoprawny_pesel(self):
        konto_niepoprwany_pesel = Konto("Jan", "Kowalski", "12345")
        self.assertEqual(konto_niepoprwany_pesel.rok_urodzenia(), "Niepoprawny pesel!", "Niepoprawny pesel został zapisany!")
        self.assertEqual(konto_niepoprwany_pesel.urodzony_po_1960(), "Niepoprawny pesel!", "Zły wynik dla niepoprawnego peselu!") 

    def test_rok_urodzenia(self):
        konto_1802 = Konto("Anon", "Anonski", "02820604718")
        self.assertEqual(konto_1802.rok_urodzenia(), 1802, "Niepoprawny rok urodzenia!")
        konto_1902 = Konto("Anon", "Anonski", "02020604718")
        self.assertEqual(konto_1902.rok_urodzenia(), 1902, "Niepoprawny rok urodzenia!")
        konto_2102 = Konto("Anon", "Anonski", "02420604718")
        self.assertEqual(konto_2102.rok_urodzenia(), 2102, "Niepoprawny rok urodzenia!")
        konto_2202 = Konto("Anon", "Anonski", "02620604718")
        self.assertEqual(konto_2202.rok_urodzenia(), 2202, "Niepoprawny rok urodzenia!")
        konto_1912 = Konto("Anon", "Anonski", "12020604718")
        self.assertEqual(konto_1912.rok_urodzenia(), 1912, "Niepoprawny rok urodzenia!")
        konto_2112 = Konto("Anon", "Anonski", "12420604718")
        self.assertEqual(konto_2112.rok_urodzenia(), 2112, "Niepoprawny rok urodzenia!")
        konto_2212 = Konto("Anon", "Anonski", "12620604718")
        self.assertEqual(konto_2212.rok_urodzenia(), 2212, "Niepoprawny rok urodzenia!")