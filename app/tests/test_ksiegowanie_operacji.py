import unittest

from ..Konto import Konto

class TestKsiegowaniaOperacji(unittest.TestCase):
    imie = "Szymon"
    nazwisko = "Kalkowski"
    pesel = "02220604718"

    def test_przelew_przychodzacy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 500
        konto.zaksieguj_przelew_przychodzacy(100)
        self.assertEqual(konto.saldo, 500+100, "Pieniądze nie wpłynęły na konto!")

    def test_przlew_wychodzacy_wystarczajacye_srodki(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 500
        konto.zaksieguj_przelew_wychodzacy(100)
        self.assertEqual(konto.saldo, 500-100, "Pieniądze nie zostały pobrane poprawnie!")
        
    def test_przelew_wychodzacy_niewystarczajace_srodki(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 500
        konto.zaksieguj_przelew_wychodzacy(600)
        self.assertEqual(konto.saldo, 500, "Przelew nie został anulowany pomimo niewystarczających środków!")
    def test_seria_przelewow(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 500
        konto.zaksieguj_przelew_wychodzacy(100)
        konto.zaksieguj_przelew_przychodzacy(200)
        konto.zaksieguj_przelew_wychodzacy(2000)
        self.assertEqual(konto.saldo, 500-100+200, "Seria przelewów niezaksięgowana poprawnie!")