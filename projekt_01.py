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
def vypis_oddelovac():
    print(79 * "-")

def ocisti_text(k_ocisteni):
    """
    Očistí zadaný text od znaků interpunkce: .,"'-?:!;
    """
    
    # toto řešení jsem našel pomocí vyhledávání, není mé
    vynechat = ".,\"'-?:!;"
    
    return "".join(znak for znak in k_ocisteni if znak not in vynechat)

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

    # slovník s počtem výsku slov jednotlivých délek, je uveden první údaj, aby bylo jasné, jaká kombinace klíč-hodnota se bude používat
    statistiky_pocty_znaku = {
        1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0,
        10: 0, 11: 0, 12: 0
    }

    # vybere text ke zpracování zadaný uživatelem z proměnné TEXTS - 1, pro pořadí od 0
    text_k_analyze = TEXTS[k_analyze - 1] 

    # očistí text o znaky interpunkce
    text_k_analyze = ocisti_text(text_k_analyze)
    
    # aktualizuje ve slovníku počet slov
    slov = len(text_k_analyze.split()) 
    statistiky.update(pocet_slov=slov)

    # for cyklus, který postupně přidá počet slov s prvním velkým, všechny velké, všechny malé a číslice
    for word in text_k_analyze.split():
        if word.istitle():
            statistiky["pocet_slov_zacina_velkym"] += 1
        elif word.isupper():
            statistiky["pocet_slov_velkymi"] += 1
        elif word.islower():
            statistiky["pocet_slov_malymi"] += 1
        elif word.isnumeric():
            statistiky["pocet_cisel"] += 1 # zvedne údaj počtu číslic
            statistiky["suma_cisel"] += int(word) # přičte hodnotu číslice

        # uloží do proměnné počet znaků procházeného slova
        pocet_znaku = len(word) # !!! ale počítá například i tečku s posledním slovem

        # pokud ve slovníku neexistuje klíč pro daný počet znaků, vytvoří jej. pokud esistuje, přičte 1 
        if not pocet_znaku in statistiky_pocty_znaku:
            statistiky_pocty_znaku[pocet_znaku] = 1
        else:
            statistiky_pocty_znaku[pocet_znaku] += 1

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
        vypis_oddelovac()
        print(f"{jmeno}, vítej v aplikaci,\nk analýze máme 3 texty.")
        vypis_oddelovac()
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
        vypis_oddelovac()
        analyzovany_text = analyzuj_text(k_analyze)
        vypis_statistiky(analyzovany_text)
        
    else:
        print("Uživatel nenalezen nebo zadáno špatné heslo. Ukončuji program")

