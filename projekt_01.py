"""
projekt_01.py: první projekt do Engeto Online Python Akademie
author: Lukáš Karásek
email: lukas@lukaskarasek.com
discord: lukaskarasek__77224
"""
# importy

# proměnné
uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# definice funkcí

def zadej_udaje():
    """
    Funkce si vyžádá od uživatele dvy vstupy, uživ. jméno a heslo. Ty pak vrátí na výstupu jako Tuple
    """
    jmeno = input("Zadej uživatelské jméno: ")
    heslo = input("Zadej heslo: ")
    return (jmeno, heslo)


def je_registrovany(jmeno, heslo):
    """
    Tato funkce vrátí True, jestliže je uživatel registrovaný
    """
    if (jmeno in uzivatele) and (heslo == uzivatele[jmeno]):
        return True
    else:
        return False


# hlavní pogram
if __name__ == "__main__":
    jmeno, heslo = zadej_udaje()
    if je_registrovany(jmeno, heslo):
        print(f"{jmeno}, vítej v aplikaci")
    else:
        print("Uživatel nenalezen nebo zadáno špatné heslo. Ukončuji program")
        
