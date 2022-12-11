import unittest
from unittest import mock

from ..KontoFirmowe import KontoFirmowe

class TestStworzKontoFirmowe(unittest.TestCase):
    @mock.patch.object(KontoFirmowe, 'request_do_api', return_value=True)
    def test_tworzenie_konta_firmowego(self, mock):
        pierwsze_konto=KontoFirmowe("Foxtry", "5831014898")
        self.assertEqual(pierwsze_konto.nazwa, "Foxtry", "Nazwa nie została zapisana!")
        self.assertEqual(pierwsze_konto.nip, "5831014898", "NIP nie został zapisany!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")

    def test_tworzenie_konta_za_krotki_nip(self):
        konto_za_ktotki_nip=KontoFirmowe("Foxtry", "2137")
        self.assertEqual(konto_za_ktotki_nip.nip, "Niepoprawny NIP!", "Za krótki NIP został zaakceptowany!")
    
    def test_tworzenie_konta_za_dlugi_nip(self):
        konto_za_dlugi_nip=KontoFirmowe("Foxtry", "1375876414755729")
        self.assertEqual(konto_za_dlugi_nip.nip, "Niepoprawny NIP!", "Za długi NIP został zaakceptowany!")

    @mock.patch.object(KontoFirmowe, 'request_do_api', return_value=False)
    def test_tworzenie_konta_firmowego_pranie(self, mock):
        konto_pranie=KontoFirmowe("Foxtry", "5831014899")
        self.assertEqual(konto_pranie.nip, "Pranie!", "Nip, którego nie ma w oficjalnej bazie danych, został zapisany!")
        