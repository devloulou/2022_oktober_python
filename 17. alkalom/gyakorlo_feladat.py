# 1. feladat: írjatok egy olyan függvényt, amely bejövő paraméterben megkap 2 számot és 1 matematikai műveletet
# A függvény adja vissza az operatorral elvégzendő művelete ereményét.
# Tartsátok be a matematika alapszabályait!

# példa függvényhívásra: my_func(1, 2, "/") -> eredmény: 0.5


# 2. feladat:  írjatok egy olyan függvényt, amivel egy kitalált tranzakciót lehetne lebonyolítani
# egy példa, hogy hogyan tároljám a tranzakció adatait
# a függvény paraméterben kapja meg a következő adatokat: kinek utalnék, mennyit
# minden utalásnál a kezdő egyenlegem legyen 200_000 Ft.
# a függvény írásakor védjük le azokat az eseteket, amelyek problémát okozhatnak:
# pl. többet utalnék, mint amennyi az egyenlegem
my_dict = {
    "transaction": {
        "transation_id": 10001,
        "sender": {
            "balance_after_transfer": 110_000,
            "balance_before_transfer": 135_000,
            "name": "Mekk Elek"
        },
        "reciever": {
            "transfer_amount": 25_000,
            "name": "Lapos Elemér"
        }
    }
}


# 3. feladat: írjatok egy olyan programot, amely a kapott mondantról eldönti, hogy palindrome-e.
# Palindrom fogalma: a szót vagy mondatot visszafelé olvasva ugyan azt kapom
# pl. szó: görög
# mondant: indul a görög aludni

# 4. feladat: írjatok egy olyan függvényt, amely tetszőleges helyre kiír egy json-t.
# figyeljetek arra, hogy kezelje le azokat az eseteket, amikor az adat nem dictionary.