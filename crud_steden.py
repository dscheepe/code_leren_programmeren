steden = ["Brussel","Amsterdam","Parijs","Rome","Madrid"]
def toon_steden():
    print("steden in lijst zijn")
    for i,stad in enumerate(steden):
        print(i,stad)

def voeg_een_stad_toe():
    nieuwe_stad = input("geef de naam van de nieuwe stad").capitalize()
    if nieuwe_stad.isalpha() and nieuwe_stad not in steden:
        steden.append(nieuwe_stad)
        print(f"{nieuwe_stad} is toegevoegd aan de lijst")
    else:
        print("bestaat al of geen geldige naam")
def wijzig_stadsnaam():
    oude_stad = input("Geef de naam in die je wenst te wijzigen")
    if oude_stad.capitalize() in steden:
        plaats_vd_stad = steden.index(oude_stad)
        steden[plaats_vd_stad] = input("geef nieuwe naam")
        #alternatief 1 regel
        #namen[namen.index(oude_naam)] = input("geef nieuwe naam")
    else:
        print("naam niet terug gevonden in de lijst")
def maak_data_string():
    return ",".join(steden)



