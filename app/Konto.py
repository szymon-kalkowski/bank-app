class Konto:
    ekspresowy_cena = 1

    def __init__(self, imie, nazwisko, pesel, kod = None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = self.walidacja_pesel(pesel)
        self.kod = kod
        self.saldo = self.walidacja_kodu_i_wieku()
        self.historia = []
        
    def walidacja_pesel(self, pesel):
        if len(pesel) == 11: 
            return pesel
        else:
            return "Niepoprawny pesel!"

    def walidacja_kodu_i_wieku(self):
        if self.kod != None and self.urodzony_po_1960():
            if len(self.kod) == 8:
                if self.kod[0:5] == "PROM_":
                    return 50
        return 0

    def rok_urodzenia(self):
        pesel = self.pesel
        if pesel != "Niepoprawny pesel!":
            if int(pesel[0])==0:
                if int(pesel[2])==8 or int(pesel[2])==9:
                    return 1800+int(pesel[1])
                if int(pesel[2])==0 or int(pesel[2])==1:
                    return 1900+int(pesel[1])
                if int(pesel[2])==2 or int(pesel[2])==3:
                    return 2000+int(pesel[1])
                if int(pesel[2])==4 or int(pesel[2])==5:
                    return 2100+int(pesel[1])
                if int(pesel[2])==6 or int(pesel[2])==7:
                    return 2200+int(pesel[1])
            elif 0<int(pesel[0]):
                if int(pesel[2])==8 or int(pesel[2])==9:
                    return 1800+int(pesel[0:2])
                if int(pesel[2])==0 or int(pesel[2])==1:
                    return 1900+int(pesel[0:2])
                if int(pesel[2])==2 or int(pesel[2])==3:
                    return 2000+int(pesel[0:2])
                if int(pesel[2])==4 or int(pesel[2])==5:
                    return 2100+int(pesel[0:2])
                if int(pesel[2])==6 or int(pesel[2])==7:
                    return 2200+int(pesel[0:2])
        return "Niepoprawny pesel!"

    def urodzony_po_1960(self):
        if isinstance(self.rok_urodzenia(), int):
            return self.rok_urodzenia() > 1960
        return "Niepoprawny pesel!"

    def zaksieguj_przelew_wychodzacy(self, wartosc):
        if wartosc <= self.saldo:
            self.saldo -= wartosc
            self.historia.append(-wartosc)

    def zaksieguj_przelew_przychodzacy(self, wartosc):
        self.saldo += wartosc
        self.historia.append(wartosc)
    
    def zaksieguj_przelew_ekspresowy(self, wartosc):
        if wartosc <= self.saldo:
            self.saldo -= wartosc + self.ekspresowy_cena
            self.historia.append(-wartosc)
            self.historia.append(-self.ekspresowy_cena)

    def zaciagnij_kredyt(self, wartosc):
        if len(self.historia) < 5:
            return False
        if self.historia[-3] > 0 and self.historia[-2] > 0 and self.historia[-1] > 0 and sum(self.historia[-5:]) > wartosc:
            self.saldo += wartosc
            return True
        return False