import unittest

from ..KontoFirmowe import KontoFirmowe

class TestStworzKontoFirmowe(unittest.TestCase):
    def test_tworzenie_konta_firmowego(self):
        pierwsze_konto=KontoFirmowe("Foxtry", "1234567890")
        self.assertEqual(pierwsze_konto.nazwa, "Foxtry", "Nazwa nie została zapisana!")
        self.assertEqual(pierwsze_konto.nip, "1234567890", "NIP nie został zapisany!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")

    def test_tworzenie_konta_za_krotki_nip(self):
        konto_za_ktotki_nip=KontoFirmowe("Foxtry", "2137")
        self.assertEqual(konto_za_ktotki_nip.nip, "Niepoprawny NIP!", "Za krótki NIP został zaakceptowany!")
    
    def test_tworzenie_konta_za_dlugi_nip(self):
        konto_za_dlugi_nip=KontoFirmowe("Foxtry", "1375876414755729")
        self.assertEqual(konto_za_dlugi_nip.nip, "Niepoprawny NIP!", "Za długi NIP został zaakceptowany!")
        