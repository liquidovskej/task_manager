ukoly = [] # zde vytvářím seznam pro úkoly

def hlavni_menu():  
    while True:     # použil jsem funkci while true, aby se menu neustále načítalo, dokud uživatel neukončí program                                   
        print("\nSprávce úkolů - Hlavní menu")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")

        volba = input("Vyberte možnost (1-4): ") # uživatel zadá vstup

        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("Program ukončen.") # volba 4
            break # break ukončí celý cyklus, tedy v tomto případěi funkci hlavní menu a tím pádem i program
        else:
            print("Neplatná volba. Zadejte prosím číslo od 1 do 4.")


def pridat_ukol(): # volba 1
    while True:
        nazev = input("Zadejte název úkolu: ")
        popis = input("Zadejte popis úkolu: ")

        if nazev == "" or popis == "": # pokud je název nebo popis prázdný, tak program upozorní
            print("Zadali jste neplatný název či popis. Prosím, zadejte znovu.")
            continue # continue mě vrací zpět na začátek cyklu

        ukoly.append({"nazev": nazev , "popis": popis}) # ukládání úkolu na konec seznamu / ukládání jako "klíč": hodnota
        print(f"Úkol '{nazev}' byl přidán.")
        return # ukončí funkci
    

def zobrazit_ukoly(): # volba 2
    if len(ukoly) == 0: # funkce len sčítá počet prvků v seznamu
        print("Seznam úkolů je prázdný.")
        return # ukončí funkci
    
    print("Seznam úkolů:")
    for i, ukol in enumerate(ukoly, start=1): # zde potřebuji přidat index, abych dle nich mohl úkol následně i odstranit, definuji proměnnou ukol a enumerate vypíše ze seznamu úkolů vše po jednom, index začínají od nuly, takže je zapotřebí zadefinovat ještě start od 1
        print(f"{i}. {ukol['nazev']} - {ukol['popis']}") # pro seznam použitý f-string (kombinuje text a proměnné), musím uvozovkami rozlišit pasáže


def odstranit_ukol(): # volba 3
    if len(ukoly) == 0:  # podmínka opětovně použita (byla použita v zobrazení úkolů)
        print("Seznam úkolů je prázdný.")
        return

    print("Seznam úkolů:")
    for i, ukol in enumerate(ukoly, start=1):
        print(f"{i}. {ukol['nazev']} - {ukol['popis']}") # opět opětovně použitá podmínka

    cislo = int(input("Zadejte číslo úkolu, který chcete odstranit: "))

    if cislo < 1 or cislo > len(ukoly):
        print("Neexistující úkol.")
        return

    odstraneny = ukoly.pop(cislo - 1) # pro pop bylo zapotřebí udělat input v INT verzi, tedy čistě číselné
    print(f"Úkol '{odstraneny['nazev']}' byl odstraněn.")



hlavni_menu()


