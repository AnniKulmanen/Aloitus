# Tähän mennessä käytettyjä funktioita
# print(X) # Tulostetaan X
# X = input() # luetaan merkkijono muuttujaan X
# str(X) # muutetaan X merkkijonoksi


def kysy_nimi():
    nimi = input("Anna nimi: ")
    return nimi


def kysy_nimet(lkm):
    nimet =[]
    while len(nimet) <lkm:
        nimi = kysy_nimi()
        nimet.append(nimi)
    return nimet


nimilista= kysy_nimet(3)
print(nimilista)