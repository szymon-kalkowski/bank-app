from .Konto import Konto

class KontoFirmowe(Konto):
    ekspresowy_cena = 5

    def __init__(self, nazwa, nip):
        self.nazwa = nazwa
        self.nip = self.walidacja_nip(nip)
        self.saldo = 0

    def walidacja_nip(self, nip):
        if len(nip) == 10: 
            return nip
        else:
            return "Niepoprawny NIP!"
