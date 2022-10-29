from .Konto import Konto

class KontoFirmowe(Konto):
    def __init__(self, nazwa, nip):
        self.nazwa = nazwa
        self.nip = self.walidacja_nip(nip)
        self.saldo = 0

    def walidacja_nip(self, nip):
        if len(nip) == 10: 
            return nip
        else:
            return "Niepoprawny NIP!"

    def zaksieguj_przelew_ekspresowy(self, wartosc):
        if wartosc <= self.saldo:
            self.saldo -= wartosc + 5
