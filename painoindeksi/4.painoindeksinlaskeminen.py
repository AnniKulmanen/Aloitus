# SOVELLUS PAINOINDEKSIN JA KEHON RASVAPROSENTIN LASKEMISEEN
# ==========================================================

# Muuttujat
# Kysytään käyttäjältä:
pituus_teksti = input ('Kuinka pitkä olet (cm): ')
paino_teksti = input ('Kuinka paljon painat (kg): ')
pituus = float(pituus_teksti) # Muutetaan liukuluvuksi
paino = float(paino_teksti) # Muutetaan liukuluvuksi

# Kaikki jotka ovat ''' ''' välissä muuttuivat kommenteiksi
'''
pituus_metreina = pituus / 100 

# Lasketaan painoindeksi (BMI)
bmi = paino / pituus_metreina **2

print('Painoindeksisi on', bmi)

'''
# Määritellään funktio painoindeksin laskentaan
def laske_bmi(paino, pituus):
    """Laskee painoinndekstin (BMI)

    Args:
        paino (float): paino (kg)
        pituus (float): pituus (cm)

    Returns:
        float: painoindeksi desimaalin tarkkuudella
    """

    pituus = pituus / 100 # muutetaan pituus metreiksi
    bmi = paino / pituus**2
    bmi = round(bmi, 1)
    return bmi 

bmi = laske_bmi(paino, pituus)

print('Laskin painoindeksisi se on', bmi)
