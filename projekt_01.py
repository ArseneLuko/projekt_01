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

# hlavní pogram
if __name__ == "__main__":
    # jmeno = input("Zadej uživatelské jméno: ")
    # heslo = input("Zadej heslo: ")
    jmeno, heslo = "bob", "123" # slouží při testování k vynechání zadávání

    # otestujeme, jestli uživatel existuje a je zadáno odpovídající heslo
    if (jmeno in uzivatele) and (heslo == uzivatele[jmeno]):
        print(f"{jmeno}, vítej v aplikaci,\nk analýze máme 3 texty.")
        k_analyze = input("Který text chceš analyzovat? Zadej číslo 1 - 3: ")
        
        # otestuje, jestli je možné převést vstup na celé číslo
        try:
            k_analyze = int(k_analyze)
        except ValueError:
            print("Je potřeba zadat celé číslo. Ukončuji program")
            quit()

        # kontrola jestli je číslo v rozmezí 1 až 3
        if k_analyze not in range(1,4):
            print("Zadané číslo bělo být v rozmezí 1 - 3. Ukončuji program")
            quit()
        
        print(f"Budeme analyzovat text číslo {k_analyze}")
        
    else:
        print("Uživatel nenalezen nebo zadáno špatné heslo. Ukončuji program")

