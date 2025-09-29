namen = ["An","Bart","Carlo","Denise","Erika","Franko","Gert"]

def toon_list():
    print("volgende namen staan in de lijst")
    for naam in namen:
        print(naam)

def voeg_naam_toe():
    naam = input("Geef een naam")
    if naam.isalpha():
        if naam.capitalize() in namen:
            print("Naam reeds in de lijst")
        else:
            namen.append(naam)
    else:
        print("naam mag enkel uit letters bevatten, geen cijfers")
def wijzig_naam():
    oude_naam = input("Geef de naam in die je wenst te wijzigen")
    if oude_naam.capitalize() in namen:
        plaats_vd_naam = namen.index(oude_naam)
        namen[plaats_vd_naam] = input("geef nieuwe naam")
        #alternatief 1 regel
        #namen[namen.index(oude_naam)] = input("geef nieuwe naam")
    else:
        print("naam niet terug gevonden in de lijst")

def verwijder_naam():
    naam_verwijderen = input("geef de naam die je wenst te verwijderen")
    if naam_verwijderen.capitalize() in namen:
        y_n = input("ben je zeker (y/n")
        if y_n.upper() == "Y":
            namen.remove(naam_verwijderen)
            print("naam is verwijderd")
    else:
        print("geen wijziging aan lijst toegebracht")
#toon_list()
voeg_naam_toe()
toon_list()
#wijzig_naam()
#toon_list()
toon_list()
verwijder_naam()
toon_list()