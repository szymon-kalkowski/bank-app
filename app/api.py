from flask import Flask, request, jsonify
from app.RejestrKont import RejestrKont
from app.Konto import Konto

app = Flask(__name__)

@app.route("/konta/stworz_konto", methods=['POST'])
def stworz_konto():
    dane = request.get_json()
    print(f"Request o stworzenie konta z danymi: {dane}")
    konto = Konto(dane["imie"], dane["nazwisko"], dane["pesel"])
    RejestrKont.dodaj_konto(konto)
    return jsonify("Konto stworzone"), 201

@app.route("/konta/ile_kont", methods=['GET'])
def ile_kont():
    return jsonify(RejestrKont.ile_kont()), 200

@app.route("/konta/konto/<pesel>", methods=['GET'])
def wyszukaj_konto_z_peselem(pesel):
    print(f"Request o konto z peselem: {pesel}")
    konto = RejestrKont.wyszukaj_konto_z_peselem(pesel)
    print(konto)
    if konto != None:
        return jsonify(imie=konto.imie, nazwisko=konto.nazwisko, pesel=konto.pesel, saldo=konto.saldo), 200
    else:
        return jsonify("Konto nie istnieje"), 404

@app.route("/konta/konto/<pesel>", methods=['PUT'])
def zaktualizuj_konto_z_peselem(pesel):
    dane=request.get_json()
    print(f"Request o aktualizację konta o peselu {pesel} z danymi: {dane}")
    konto = RejestrKont.zaktualizuj_konto_z_peselem(pesel, dane)
    print(konto)
    if konto != None:
        return jsonify("Aktualizacja zakończona pomyślnie"), 200
    else:
        return jsonify("Konto nie istnieje"), 404

@app.route("/konta/konto/<pesel>", methods=['DELETE'])
def usun_konto_z_peselem(pesel):
    print(f"Request o usunięcie konta o peselu {pesel}") 
    RejestrKont.usun_konto_z_peselem(pesel)
    return jsonify("Usunięcie zakończone pomyślnie"), 200