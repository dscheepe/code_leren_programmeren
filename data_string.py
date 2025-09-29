#van list naar string
steden = ["Genk","Hasselt","Pelt","As","Lanaken"]
datastring = ",".join(steden)
woord_gespeld = ["B","a","l","l","o","n"]
woord = "".join(woord_gespeld)
print(woord)
#string naar een list. vb een csv lijn
string_met_data = "ID,NAAM,LEEFTIJD PERSOON,GESLACHT,AFDELING,MAANDLOON"
kolommen = string_met_data.split(",")
#verander een kolom van naam
for e,kolom in enumerate(kolommen):
    print(e,kolom)
kol_nummer = int(input("welk kolom nummer"))
if kol_nummer < len(kolommen):
    kolommen[kol_nummer] = input("geef nieuwe kolomnaam")
else:
    print("kolomnaam kon niet aangepast worden")
print(kolommen)

