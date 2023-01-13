Feature: Account registry

    Scenario: User is able to create a new account
        Given Number of accounts in registry equals: "0"
        When I create an account using name: "kurt", last name: "cobain", pesel: "89091209875"
        Then Number of accounts in registry equals: "1"
        And Account with pesel "89091209875" exists in registry
    
    Scenario: User is able to create a second account
        Given Number of accounts in registry equals: "1"
        When I create an account using name: "Szymon", last name: "Kalkowski", pesel: "02220604718"
        Then Number of accounts in registry equals: "2"
        And Account with pesel "02220604718" exists in registry

    Scenario: User is able to delete already created account
        Given Account with pesel "89091209875" exists in registry
        When I delete account with pesel: "89091209875"
        Then Account with pesel "89091209875" does not exists in registry
    
    Scenario: User is able to update last name saved in account
        Given Account with pesel "02220604718" exists in registry
        When I update last name with pesel "02220604718" to "Kowalski"
        Then Last name in account with pesel "02220604718" is "Kowalski"

    Scenario: Admin user is able to clear the account registry
        When I clear the account registry
        Then Number of accounts in registry equals: "0"