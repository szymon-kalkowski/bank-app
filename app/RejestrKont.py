class RejestrKont():
    lista = []

    @classmethod
    def dodaj_konto(cls, konto):
        for i in cls.lista:
            if i.pesel == konto.pesel:
                return None
        cls.lista.append(konto)
        return konto

    @classmethod
    def ile_kont(cls):
        return len(cls.lista)

    @classmethod
    def wyszukaj_konto_z_peselem(cls, pesel):
        for i in cls.lista: 
            if i.pesel == pesel:
                return i
        return None

    @classmethod
    def zaktualizuj_konto_z_peselem(cls, pesel, dane):
        konto = cls.wyszukaj_konto_z_peselem(pesel)
        if konto != None:
            konto.imie = dane['imie'] if 'imie' in dane else konto.imie
            konto.nazwisko = dane['nazwisko'] if 'nazwisko' in dane else konto.nazwisko
            konto.pesel = dane['pesel'] if 'pesel' in dane else konto.pesel
            konto.saldo = dane['saldo'] if 'saldo' in dane else konto.saldo
        return konto

    @classmethod
    def usun_konto_z_peselem(cls, pesel):
        konto = cls.wyszukaj_konto_z_peselem(pesel)
        if konto != None:
            cls.lista.remove(konto)
        return konto

    @classmethod
    def usun_wszystkie_konta(cls):
        cls.lista = []
        return cls.lista
            