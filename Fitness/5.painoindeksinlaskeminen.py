# SOVELLUS PAINOINDEKSIN JA KEHON RASVAPROSENTIN LASKEMISEEN
# ==========================================================

# Muuttujat
# Kysytään käyttäjältä:
pituus = float (input ('Kuinka pitkä olet (cm): '))
paino = float (input ('Kuinka paljon painat (kg): '))

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
