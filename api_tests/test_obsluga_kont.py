import unittest
import requests

class TestObslugaKont(unittest.TestCase):
    body = {
        'imie': 'nick',
        'nazwisko': 'cave',
        'pesel': '02220604718'
    }

    data = {
        'imie': 'Szymon',
        'saldo': 30
    }

    url = 'http://localhost:5000'

    def test_1_tworzenie_kont_poprawne(self):
        create_resp = requests.post(self.url + '/konta/stworz_konto', json=self.body)
        self.assertEqual(create_resp.status_code, 201)

    def test_2_get_po_peselu(self):
        get_resp = requests.get(self.url + f"/konta/konto/{self.body['pesel']}")
        self.assertEqual(get_resp.status_code, 200)
        resp_body = get_resp.json()
        self.assertEqual(resp_body["nazwisko"], self.body["nazwisko"])
        self.assertEqual(resp_body["imie"], self.body["imie"])
        self.assertEqual(resp_body["saldo"], 0)

    def test_3_update_po_peselu(self):
        put_resp = requests.put(self.url + f"/konta/konto/{self.body['pesel']}", json=self.data)
        self.assertEqual(put_resp.status_code, 200)
        get_resp = requests.get(self.url + f"/konta/konto/{self.body['pesel']}")
        self.assertEqual(get_resp.status_code, 200)
        resp_body = get_resp.json()
        self.assertEqual(resp_body["imie"], self.data["imie"])
        self.assertEqual(resp_body["nazwisko"], self.body["nazwisko"])
        self.assertEqual(resp_body["pesel"], self.body["pesel"])
        self.assertEqual(resp_body["saldo"], self.data["saldo"])

    def test_4_delete_po_peselu(self):
        ile_kont = int(requests.get(self.url + f"/konta/ile_kont").json())
        resp_del = requests.delete(self.url + f"/konta/konto/{self.body['pesel']}")
        self.assertEqual(resp_del.status_code, 200)
        ile_kont_po = int(requests.get(self.url + f"/konta/ile_kont").json())
        self.assertEqual(ile_kont_po + 1, ile_kont)

    def test_5_dodanie_konta_ktore_istnieje(self):
        create_resp = requests.post(self.url + '/konta/stworz_konto', json=self.body)
        self.assertEqual(create_resp.status_code, 201)
        create_resp = requests.post(self.url + '/konta/stworz_konto', json=self.body)
        self.assertEqual(create_resp.status_code, 400)

        