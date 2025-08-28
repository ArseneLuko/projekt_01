# Textový analyzátor
## Projekt na kurzu Pythonu na portálu ENGETO (engeto.cz)

Zadáním bylo vytvořit textový analyzátor, který vyzve uživatele k přihlášení (zadaný seznam uživatelů), vyzve uživatele k výběru z dostupných textů a vypíše pro text:
1. počet slov
2. počet slov začínajících velkými písmeny
3. počet slov psaných velkými písmeny
4. počet slov psaných malými písmeny
5. počet čísel (ne cifer)
6. sumu všech čísel (ne cifer) v textu

Skript vykreslí graficky počet výskytů délek jednotlivých slov

## Přidání vlastních textů
Vlastní text je možné přidat do souboru `text.py` do proměnné `TEXTY`

## Hodnocení od lektora: SPLNĚNO

### Co se mi líbilo: 
1. Projekt je velice dobře strukturovaný, použitím vlastním funkcí, zlepšuješ čitelnost a modularitu kódu
2. Přihlášení je funkční, efektivně kontroluješ správnost údajů.
3. Ošetřeny uživatelské vstupy pro výběr textu. Opět hezky řešeno a efektivně
4. Statistiky procházíš jedním for cyklem, což je efektivní
5. Odstranění nežádoucích znaků, bereš v potaz i znaky, které tam aktuálně nejsou, ale můžou být
6. Hezký výpis grafu, je formátovaný


### Co by jsi měl/a zlepšit: Co zlepšit:
1. Jediné doporučení co bych dal je, udělat univerzální výběr textu. V případě přidání dalších textů, by si musel opravit podmínku na řádku 131. Teď jí máš definovanou na tři texty

*poznámka autora: funkce přidána, nyní ř. 136 (28. 8. 2025)*

### Závěr: 
Projekt je skvěle napsaný a převyšuje požadavky zadání. Gratuluji, projekt schvaluji. Skvělá práce
