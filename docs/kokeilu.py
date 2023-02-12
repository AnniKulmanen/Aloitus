print("moi")
print("hei")

nimet = ["Keijo", "Kiia", "Vieno"]

for ihminen in ["Keijo", "Kiia", "Vieno", ""]:
    print("Hei" , ihminen)
    print("Nimessäsi on", len (ihminen), "kirjainta")

luku =42
print("Luku on", luku)

# Merkkijonot (string) voidaaan kirjoittaa 
# lainausmerkeillä (") tai heittomerkeillä (')
merkkijono = "Punainen"
merkkijono2 = 'Sininen'

print("Merkkijonot ovat:", merkkijono, "ja", merkkijono2)

lista = [
    #Merkkijonot voi olla samassa listassa
    "Merkkijono", 
    # kuin listoja tai lukuja
    [1, 2, 3,]
]

print(lista)

sanakirja = {
    "väri": "punainen",
    "koko": "pieni", 
    "pituus": 152
}

print(sanakirja)

print(sanakirja["koko"])
print(sanakirja.keys())
print(sanakirja.values())

otsikot = [
    {"taso": 1, "muotoilu": "ISO", "teksti": "Opi ohjelmoimaan"},
    {"taso": 2, "muotoilu": "Iso alkukirjain",
    "teksti": "Python-ohjelmoinnin perusteet"},
    {"taso": 1, "muotoilu": "ISO", "teksti": "Elämän tarkoitus"},
    {"taso": 2, "muotoilu": "", "teksti": "Kuinka löytää elämän tarkoitus"},
    {"taso": 3, "muotoilu": "", "teksti": "Mistä tietää?"},
]

for otsikko in otsikot:
    taso = otsikko["taso"]
    sisennys = taso * "    " # Neljä välilyöntiä toisteaan 'taso" kertaa
    teksti = otsikko["teksti"]

    if otsikko["muotoilu"] == "ISO":
        teksti = teksti.upper()
        teksti = "*** " + teksti + " ***"

    if otsikko["muotoilu"] == "Iso alkukirjain":
        teksti = teksti.title()

    print(sisennys, teksti)
