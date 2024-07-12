"""
projekt_01.py: první projekt do Engeto Online Python Akademie
author: Lukáš Karásek
email: lukas@lukaskarasek.com
discord: lukaskarasek__77224
"""
# importy
from curses.ascii import islower, isupper
from turtle import isdown
from task_template import TEXTS

# proměnné
uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# definice funkcí
def analyzuj_text(k_analyze: int):
    """
    Analyzuje text z proměnné TEXTY. Funkce vrátí slovník s údaji a slovník s počtem slov každé délky.
    1. počet slov
    2. počet slov začínajících velkými písmeny
    3. počet slov psaných velkými písmeny
    4. počet slov psaných malými písmeny
    5. počet čísel (ne cifer)
    6. sumu všech čísel (ne cifer) v textu
    """

    statistiky = {
        "pocet_slov": 0,
        "pocet_slov_zacina_velkym": 0,
        "pocet_slov_velkymi": 0,
        "pocet_slov_malymi": 0, 
        "pocet_cisel": 0, 
        "suma_cisel": 0
    }
    text_k_analyze = TEXTS[k_analyze - 1] # vybere text ke zpracování
    
    # aktualizuje ve slovníku počet slov
    slov = len(text_k_analyze.split()) 
    statistiky.update(pocet_slov=slov)

    # for cyklus, který postupně přidá počet slov s prvním velkým, všechny velké a všechny malé
    for word in text_k_analyze.split():
        if word.istitle():
            statistiky["pocet_slov_zacina_velkym"] += 1
        elif word.isupper():
            statistiky["pocet_slov_velkymi"] += 1
        elif word.islower():
            statistiky["pocet_slov_malymi"] += 1
        elif word.isnumeric():
            statistiky["pocet_cisel"] += 1
            statistiky["suma_cisel"] += int(word)

    return statistiky

def vypis_statistiky(statistiky):
    print(f"Počet slov v textu je: {statistiky['pocet_slov']},")
    print(f"z toho {statistiky['pocet_slov_zacina_velkym']} začíná velkým písmenem.")
    print(f"Počet slov psaných velkými písmeny: {statistiky['pocet_slov_velkymi']}")
    print(f"Počet slov psaných malými písmeny: {statistiky['pocet_slov_malymi']}")
    print(f"Počet čísel v textu: {statistiky['pocet_cisel']}")
    print(f"Součet těchto čísel se rovná: {statistiky['suma_cisel']}")

# hlavní pogram
if __name__ == "__main__":
    # jmeno = input("Zadej uživatelské jméno: ")
    # heslo = input("Zadej heslo: ")
    jmeno, heslo = "bob", "123" # slouží při testování k vynechání zadávání

    # otestujeme, jestli uživatel existuje a je zadáno odpovídající heslo
    if (jmeno in uzivatele) and (heslo == uzivatele[jmeno]):
        print(f"{jmeno}, vítej v aplikaci,\nk analýze máme 3 texty.")
        # k_analyze = input("Který text chceš analyzovat? Zadej číslo 1 - 3: ")
        k_analyze = 1 # slouží při testování k vynechání zadávání
        # otestuje, jestli je možné převést vstup na celé číslo
        try:
            k_analyze = int(k_analyze)
        except ValueError:
            print("Je potřeba zadat celé číslo. Ukončuji program")
            quit()

        # kontrola jestli je číslo v rozmezí 1 až 3
        if k_analyze not in range(1,4):
            print("Zadané číslo musí být v rozmezí 1 - 3. Ukončuji program")
            quit()
        
        print(f"Budeme analyzovat text číslo {k_analyze}")
        analyzovany_text = analyzuj_text(k_analyze)
        vypis_statistiky(analyzovany_text)
        
    else:
        print("Uživatel nenalezen nebo zadáno špatné heslo. Ukončuji program")

