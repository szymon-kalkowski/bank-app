import unittest

from ..Konto import Konto
from ..KontoFirmowe import KontoFirmowe

class TestKsiegowaniaPrzelewowEkspresowychKonta(unittest.TestCase):
    def test_przelew_ekspresowy_konta(self):
        konto = Konto("Szymon", "Kalkowski", "02220604718")
        konto.saldo = 500
        konto.zaksieguj_przelew_ekspresowy(200)
        self.assertEqual(konto.saldo, 500-200-1, "Pieniądze nie zostały pobrane poprawnie!")

    def test_przelew_ekspresowy_konta_ponizej_zera(self):
        konto2 = Konto("Robert", "Makłowicz", "12345678912")
        konto2.saldo = 500
        konto2.zaksieguj_przelew_ekspresowy(500)
        self.assertEqual(konto2.saldo, 500-500-1, "Pieniądze nie zostały pobrane poprawnie!")

    def test_przelew_ekspresowy_konta_niewystarczajace_srodki(self):
        konto3 = Konto("Robert", "Kubica", "12345678934")
        konto3.saldo = 500
        konto3.zaksieguj_przelew_ekspresowy(550)
        self.assertEqual(konto3.saldo, 500, "Pieniądze zostały pobrane pomimo niewystaczających środków!")

class TestKsiegowaniaPrzelewowEkspresowychKontaFirmowego(unittest.TestCase):
    def test_przelew_ekspresowy_konta_firmowego(self):
        konto_firmowe = KontoFirmowe("Foxtry", "0222060471")
        konto_firmowe.saldo = 500
        konto_firmowe.zaksieguj_przelew_ekspresowy(200)
        self.assertEqual(konto_firmowe.saldo, 500-200-5, "Pieniądze nie zostały pobrane poprawnie!")

    def test_przelew_ekspresowy_konta_firmowego_ponizej_zera(self):
        konto_firmowe2 = KontoFirmowe("Tesla", "1234567893")
        konto_firmowe2.saldo = 6000
        konto_firmowe2.zaksieguj_przelew_ekspresowy(6000)
        self.assertEqual(konto_firmowe2.saldo, 6000-6000-5, "Pieniądze nie zostały pobrane poprawnie!")

    def test_przelew_ekspresowy_konta_firmowego_niewystarczajace_srodki(self):
        konto_firmowe3 = KontoFirmowe("SpaceX", "1234567896")
        konto_firmowe3.saldo = 2500
        konto_firmowe3.zaksieguj_przelew_ekspresowy(2550)
        self.assertEqual(konto_firmowe3.saldo, 2500, "Pieniądze zostały pobrane pomimo niewystaczających środków!")

