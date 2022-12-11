import unittest
from unittest import mock

from ..Konto import Konto
from ..KontoFirmowe import KontoFirmowe

class TestHistoriiPrzelewowKonta(unittest.TestCase):
    def test_historia_przelewow_wychodzacych_konta(self):
        konto_przelewy_wychodzace = Konto("Szymon", "Kalkowski", "02220604718")
        konto_przelewy_wychodzace.saldo = 2000
        konto_przelewy_wychodzace.zaksieguj_przelew_wychodzacy(500)
        konto_przelewy_wychodzace.zaksieguj_przelew_wychodzacy(200)
        konto_przelewy_wychodzace.zaksieguj_przelew_wychodzacy(600)
        konto_przelewy_wychodzace.zaksieguj_przelew_wychodzacy(2000)
        self.assertEqual(konto_przelewy_wychodzace.historia, [-500, -200, -600], "Niepoprawna historia przelewów!")

    def test_historia_przelewow_przychodzacych_konta(self):
        konto_przelewy_przychodzace = Konto("Szymon", "Kalkowski", "02220604718")
        konto_przelewy_przychodzace.zaksieguj_przelew_przychodzacy(300)
        konto_przelewy_przychodzace.zaksieguj_przelew_przychodzacy(500)
        konto_przelewy_przychodzace.zaksieguj_przelew_przychodzacy(100)
        self.assertEqual(konto_przelewy_przychodzace.historia, [300, 500, 100], "Niepoprawna historia przelewów!")

    def test_historia_przelewow_ekspresowych_konta(self):
        konto_przelewy_ekspresowe = Konto("Szymon", "Kalkowski", "02220604718")
        konto_przelewy_ekspresowe.saldo = 3000
        konto_przelewy_ekspresowe.zaksieguj_przelew_ekspresowy(700)
        konto_przelewy_ekspresowe.zaksieguj_przelew_ekspresowy(900)
        konto_przelewy_ekspresowe.zaksieguj_przelew_ekspresowy(850)
        konto_przelewy_ekspresowe.zaksieguj_przelew_ekspresowy(2000)
        self.assertEqual(konto_przelewy_ekspresowe.historia, [-700, -1, -900, -1, -850, -1], "Niepoprawna historia przelewów!")

    def test_historia_przelewow_mieszanych_konta(self):
        konto_przelewy_mieszane = Konto("Szymon", "Kalkowski", "02220604718")
        konto_przelewy_mieszane.saldo = 1000
        konto_przelewy_mieszane.zaksieguj_przelew_przychodzacy(400)
        konto_przelewy_mieszane.zaksieguj_przelew_wychodzacy(800)
        konto_przelewy_mieszane.zaksieguj_przelew_ekspresowy(50)
        konto_przelewy_mieszane.zaksieguj_przelew_wychodzacy(700)
        self.assertEqual(konto_przelewy_mieszane.historia, [400, -800, -50, -1], "Niepoprawna historia przelewów!")

class TestHistoriiPrzelewowKontaFirmowego(unittest.TestCase):
    @mock.patch.object(KontoFirmowe, 'request_do_api', return_value=True)
    def test_historia_przelewow_wychodzacych_konta_firmowego(self, mock):
        konto_firmowe_przelewy_wychodzace = KontoFirmowe("Foxtry", "5831014898")
        konto_firmowe_przelewy_wychodzace.saldo = 2000
        konto_firmowe_przelewy_wychodzace.zaksieguj_przelew_wychodzacy(500)
        konto_firmowe_przelewy_wychodzace.zaksieguj_przelew_wychodzacy(200)
        konto_firmowe_przelewy_wychodzace.zaksieguj_przelew_wychodzacy(600)
        konto_firmowe_przelewy_wychodzace.zaksieguj_przelew_wychodzacy(2000)
        self.assertEqual(konto_firmowe_przelewy_wychodzace.historia, [-500, -200, -600], "Niepoprawna historia przelewów!")

    @mock.patch.object(KontoFirmowe, 'request_do_api', return_value=True)
    def test_historia_przelewow_przychodzacych_konta_firmowego(self, mock):
        konto_firmowe_przelewy_przychodzace = KontoFirmowe("Foxtry", "5831014898")
        konto_firmowe_przelewy_przychodzace.zaksieguj_przelew_przychodzacy(300)
        konto_firmowe_przelewy_przychodzace.zaksieguj_przelew_przychodzacy(500)
        konto_firmowe_przelewy_przychodzace.zaksieguj_przelew_przychodzacy(100)
        self.assertEqual(konto_firmowe_przelewy_przychodzace.historia, [300, 500, 100], "Niepoprawna historia przelewów!")

    @mock.patch.object(KontoFirmowe, 'request_do_api', return_value=True)
    def test_historia_przelewow_ekspresowych_konta_firmowego(self, mock):
        konto_firmowe_przelewy_ekspresowe = KontoFirmowe("Foxtry", "5831014898")
        konto_firmowe_przelewy_ekspresowe.saldo = 3000
        konto_firmowe_przelewy_ekspresowe.zaksieguj_przelew_ekspresowy(700)
        konto_firmowe_przelewy_ekspresowe.zaksieguj_przelew_ekspresowy(900)
        konto_firmowe_przelewy_ekspresowe.zaksieguj_przelew_ekspresowy(850)
        konto_firmowe_przelewy_ekspresowe.zaksieguj_przelew_ekspresowy(2000)
        self.assertEqual(konto_firmowe_przelewy_ekspresowe.historia, [-700, -5, -900, -5, -850, -5], "Niepoprawna historia przelewów!")

    @mock.patch.object(KontoFirmowe, 'request_do_api', return_value=True)
    def test_historia_przelewow_mieszanych_konta_firmowego(self, mock):
        konto_firmowe_przelewy_mieszane = KontoFirmowe("Foxtry", "5831014898")
        konto_firmowe_przelewy_mieszane.saldo = 1000
        konto_firmowe_przelewy_mieszane.zaksieguj_przelew_przychodzacy(400)
        konto_firmowe_przelewy_mieszane.zaksieguj_przelew_wychodzacy(800)
        konto_firmowe_przelewy_mieszane.zaksieguj_przelew_ekspresowy(50)
        konto_firmowe_przelewy_mieszane.zaksieguj_przelew_wychodzacy(700)
        self.assertEqual(konto_firmowe_przelewy_mieszane.historia, [400, -800, -50, -5], "Niepoprawna historia przelewów!")

