tekst = "dit is  een tekst  met  daarin  meerdere dubbele  spaties"
tekst2 = "dit is een\n\ntekst met meerdere\n\nalinea of\nenters"
tekst_clean = tekst.replace("  "," ")
print(tekst_clean)
tekst2 = tekst2.replace("\n\n","\n")
print(tekst2)