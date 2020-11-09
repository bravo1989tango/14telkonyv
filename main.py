"""
def inputlista():
    return "1,olvasás\n2,írás\n3,kilépés"

def menulista():
    menulist = ["1","2","3"]
    return menulist

def printlista():
    return "1-3 ig adj meg egy számot"

def alap_validalas():
    while True:
        menu_input = input(inputlista())
        if menu_input not in menulista():
            print(printlista())
        else:
            return menu_input
"""

telefonkonyv = {"Laci": "06701234567", "Kati": "06301234568", "Józsi": "06907894563"}

def lista():
    return int(input("1,olvasás\n2,irás\n3,kilépés\n"))

def bevitel():
    while True:
        try:
            return lista()
        except ValueError:
            print("Érvénytelen bevitel!")

    #első elem plusz vágjuk le, többit átalakitjuk integerré
    #trukk = "+36703114455"
    #print(trukk[1:])

def telszam():
    szam = input("Kérem a számot: ")
    try:
        if szam[0] == "+":
            int(szam[1:])
            return szam
        int(szam)
        return szam
    except ValueError:
        print("Próbáld újra: +36301234567")

def nevolvas():
    print(telefonkonyv.keys())
    adat = input("Név = ?: ")
    if adat in telefonkonyv:
        return telefonkonyv[adat]
    else:
        return print("A listából válassz, próbáld újra!")

def main():
    akcio = bevitel()
    while True:
        if akcio == 1:
            nevek = nevolvas()
            print(nevek)
        elif akcio == 2:
            nev = input("Add meg a nevet: ")
            szam = telszam()
            telefonkonyv.update({nev: szam})
            print(telefonkonyv)
        elif akcio == 3:
            break

main()

#házi olvasásnál felajánljuk a neveket, kiprinteljük és a
# név választásnál megnézzük hogy benne van-e a telefonkönyvben

#másik házi a videó végén

#számkitalálós játékot dinamikus függvényesitstük (plusz házi)