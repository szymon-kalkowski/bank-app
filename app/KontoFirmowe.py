import requests
import os
from datetime import date
from .Konto import Konto

class KontoFirmowe(Konto): # pragma: no cover
    ekspresowy_cena = 5

    def __init__(self, nazwa, nip):
        self.nazwa = nazwa
        self.nip = self.walidacja_nip(nip)
        self.saldo = 0
        self.historia = []
        self.wiadomosc = "Historia konta Twojej firmy to: "

    def walidacja_nip(self, nip):
        if len(nip) == 10: 
            if self.czy_nip_istnieje(nip):
                return nip
            else:
                return "Pranie!"
        else:
            return "Niepoprawny NIP!"

    def spelnia_warunki_kredytu(self, wartosc):
        if (wartosc*2 < self.saldo 
        and -1775 in self.historia):
            return True
        return False 

    @classmethod
    def czy_nip_istnieje(cls, nip):
        gov_url = os.getenv('BANK_APP_MF_URL', 'https://wl-test.mf.gov.pl/')
        data = date.today()
        url = f"{gov_url}api/search/nip/{nip}?date={data}"
        return cls.request_do_api(url)
    
    @classmethod
    def request_do_api(cls, url):
        return requests.get(url).status_code == 200
