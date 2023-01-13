from behave import *
from selenium.webdriver.common.keys import Keys
import requests
from unittest_assertions import AssertEqual

assert_equal = AssertEqual()
URL = "http://localhost:5000"

@step('Number of accounts in registry equals: "{count}"')
def ile_kont(context, count):
    get_resp = requests.get(URL + "/konta/ile_kont")
    assert_equal(get_resp.json(), int(count))

@when('I create an account using name: "{name}", last name: "{last_name}", pesel: "{pesel}"')
def utworz_konto(context, name, last_name, pesel):
    json_body = { "imie": f"{name}",
    "nazwisko": f"{last_name}",
    "pesel": f"{pesel}" 
    }
    create_resp = requests.post(URL + "/konta/stworz_konto", json = json_body)
    assert_equal(create_resp.status_code, 201)

@step('Account with pesel "{pesel}" exists in registry')
def sprawdz_czy_konto_z_pesel_istnieje(context, pesel):
    get_resp = requests.get(URL + f"/konta/konto/{pesel}")
    assert_equal(get_resp.status_code, 200)

@when('I delete account with pesel: "{pesel}"')
def usun_konto(context, pesel):
    get_resp = requests.delete(URL + f"/konta/konto/{pesel}")
    assert_equal(get_resp.status_code, 200)

@step('Account with pesel "{pesel}" does not exists in registry')
def sprawdz_czy_konto_z_pesel_nie_istnieje(context, pesel):
    get_resp = requests.get(URL + f"/konta/konto/{pesel}")
    assert_equal(get_resp.status_code, 404)

@when('I update last name with pesel "{pesel}" to "{new_last_name}"')
def zaktualizuj_nazwisko_konta(context, pesel, new_last_name):
    get_resp = requests.put(URL + f"/konta/konto/{pesel}", json={"nazwisko" : new_last_name})
    assert_equal(get_resp.status_code, 200)

@step('Last name in account with pesel "{pesel}" is "{last_name}"')
def sprawdz_zgodnosc_nazwiska(context, pesel, last_name):
    get_resp = requests.get(URL + f"/konta/konto/{pesel}")
    assert_equal(get_resp.json()['nazwisko'], last_name)

@when('I clear the account registry')
def usun_wszystkie_konta(context):
    get_resp = requests.delete(URL  + f"/konta/usun")
    assert_equal(get_resp.status_code, 200)
