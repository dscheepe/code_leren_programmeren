tekst = "dit is een hele hele lange tekst met allemaal gekke tekens akgjioaeshgfiehfiodhfidskfhsklfhsdklfnhsdklfhsndsdkjfgpsdkj"
print(len(tekst))
verhaaltje = "er was eens een. en ze ging naar het bos. toen kwam de. en ze leefden nog lang en gelukkig"
verhaaltje = verhaaltje.title()
print(verhaaltje.count("E"))
naam = "anna"
zoek_namen = ["anne","arne","an","andre","andries","anke"]
zoek = input("geef zoekopdracht")
results = []
for name in zoek_namen:
    if name.startswith(zoek):
        results.append(name)
print(results)