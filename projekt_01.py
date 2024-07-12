"""
projekt_01.py: první projekt do Engeto Online Python Akademie
author: Lukáš Karásek
email: lukas@lukaskarasek.com
discord: lukaskarasek__77224
"""
# importy
from task_template import TEXTS

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
    
def vyber_text():
    while True:
        vstup = input("Který text chceš analyzovat? Zadej číslo 1 - 3: ")
        
        try: # otestuje, jestli je možné převést vstup na celé číslo
            vstup = int(vstup)
        except ValueError:
            print("Je potřeba zadat celé číslo")
            continue

        # kontrola jestli je číslo v rozmezí 1 až 3
        if vstup not in range(1,4):
            print("Zadané číslo musí být v rozmezí 1 - 3.")
            continue

        return vstup

# hlavní pogram
if __name__ == "__main__":
    #jmeno, heslo = zadej_udaje()
    jmeno, heslo = "bob", "123" # slouží při testování k vynechání zadávání
    if je_registrovany(jmeno, heslo):
        print(f"{jmeno}, vítej v aplikaci,\nk analýze máme 3 texty.")
        k_analyze = vyber_text()
        print(f"Budeme analyzovat text číslo {k_analyze}")
    else:
        print("Uživatel nenalezen nebo zadáno špatné heslo. Ukončuji program")