"""
main.py / Textový analyzátor : První projekt kurzu Engeto - Python
author: Lukáš Karásek
email: lukas@lukaskarasek.cz
discord: lukaskarasek_arsene
"""

from task_template import TEXTS

# uživatelé ze zadání úkolu
uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}
pocet_textu_k_analyze = 0

def vypis_oddelovac():
    """
    Vypíše řadu 79 pomlček
    """
    print(79 * "-")

def ocisti_text(k_ocisteni: str) -> str:
    """
    Očistí zadaný text od znaků interpunkce: .,"'-?:!;
    """

    # toto řešení jsem našel pomocí vyhledávání, není mé
    vynechat = ".,\"'-?:!;"
    return "".join(znak for znak in k_ocisteni if znak not in vynechat)

def analyzuj_text(k_analyze: int):
    """
    Analyzuje poskytnutý text. Funkce vrátí slovník s údaji a slovník s počtem slov každé délky.
    1. počet slov
    2. počet slov začínajících velkými písmeny
    3. počet slov psaných velkými písmeny
    4. počet slov psaných malými písmeny
    5. počet čísel (ne cifer)
    6. sumu všech čísel (ne cifer) v textu
    """

    # slovník pro uložení dat
    statistiky = {
        "pocet_slov": 0,
        "pocet_slov_zacina_velkym": 0,
        "pocet_slov_velkymi": 0,
        "pocet_slov_malymi": 0, 
        "pocet_cisel": 0, 
        "suma_cisel": 0
    }

    # slovník s počtem výsku slov jednotlivých délek
    statistiky_pocty_znaku = {}

    # vybere text ke zpracování zadaný uživatelem z proměnné TEXTS - 1, pro pořadí od 0
    text_k_analyze = TEXTS[k_analyze - 1] 

    # očistí text o znaky interpunkce
    text_k_analyze = ocisti_text(text_k_analyze)
    
    # aktualizuje ve slovníku počet slov
    statistiky.update(pocet_slov=len(text_k_analyze.split()))

    # for cyklus, který postupně uloží do slovníku počet slov s prvním velkým, všechny velké, všechny malé a číslice (a ty také sečte)
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

        # uloží do proměnné počet znaků procházeného slova
        pocet_znaku = len(word)

        # pokud ve slovníku neexistuje klíč pro daný počet znaků, vytvoří jej a přiřadí první výskyt, pokud klíč esistuje, zvýší hodnotu o 1 
        if not pocet_znaku in statistiky_pocty_znaku:
            statistiky_pocty_znaku[pocet_znaku] = 1
        else:
            statistiky_pocty_znaku[pocet_znaku] += 1

    return statistiky, statistiky_pocty_znaku

def vypis_statistiky(statistiky):
    print(f"Počet slov v textu je: {statistiky['pocet_slov']}, z toho: ")
    print(f"Počet slov začínajících velkým písmenem: {statistiky['pocet_slov_zacina_velkym']}")
    print(f"Počet slov psaných velkými písmeny: {statistiky['pocet_slov_velkymi']}")
    print(f"Počet slov psaných malými písmeny: {statistiky['pocet_slov_malymi']}")
    print(f"Počet čísel v textu: {statistiky['pocet_cisel']}")
    print(f"Součet těchto čísel se rovná: {statistiky['suma_cisel']}")

def vypis_delky_slov(pocty_znaku):
    pocty_znaku = dict(sorted(pocty_znaku.items()))

    print(f"|{'Výskyt délek slov v textu': ^36}|")
    print(f"|{36 * '-'}|")
    print(f"| délka | {'výskyt znaků:': <18} | počet |")
    znak = "*" 
    for delka, vyskyt in pocty_znaku.items():
        print(f"|{delka: >6} |{znak * vyskyt: <20}| {vyskyt: <6}|")

# hlavní pogram
if __name__ == "__main__":
    vypis_oddelovac()
    jmeno = input("Zadej uživatelské jméno: ")
    heslo = input("Zadej heslo: ")
    # jmeno, heslo = "bob", "123" # slouží při testování k vynechání zadávání

    pocet_textu_k_analyze = len(TEXTS)

    # otestujeme, jestli uživatel existuje a je zadáno odpovídající heslo
    if (jmeno in uzivatele) and (heslo == uzivatele[jmeno]):
        vypis_oddelovac()
        print(f"{jmeno}, vítej v aplikaci,\nk analýze máme {pocet_textu_k_analyze} texty.")
        vypis_oddelovac()
        k_analyze = input(f"Který text chceš analyzovat? Zadej číslo 1 - {pocet_textu_k_analyze}: ")
        # k_analyze = 1 # slouží při testování k vynechání zadávání

        # otestuje, jestli je možné převést vstup na celé číslo
        try:
            k_analyze = int(k_analyze)
        except ValueError:
            print("Je potřeba zadat celé číslo. Ukončuji program")
            quit()

        # kontrola jestli je číslo v rozmezí 1 až počet textů
        if k_analyze not in range(1,pocet_textu_k_analyze + 1):
            print(f"Zadané číslo musí být v rozmezí 1 - {pocet_textu_k_analyze}. Ukončuji program")
            quit()
        
        print(f"Budeme analyzovat text číslo: {k_analyze}")
        vypis_oddelovac()
        analyzovany_text, pocty_znaku = analyzuj_text(k_analyze)
        vypis_statistiky(analyzovany_text)
        vypis_oddelovac()
        vypis_delky_slov(pocty_znaku)
        vypis_oddelovac()
        
    else:
        print("Uživatel nenalezen nebo zadáno špatné heslo. Ukončuji program")