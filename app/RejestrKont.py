class RejestrKont():
    lista = []

    @classmethod
    def dodaj_konto(cls, konto):
        cls.lista.append(konto)

    @classmethod
    def ile_kont(cls):
        return len(cls.lista)

    @classmethod
    def wyszukaj_konto_z_peselem(cls, pesel):
        for i in cls.lista: 
            if i.pesel == pesel:
                return i
        return None