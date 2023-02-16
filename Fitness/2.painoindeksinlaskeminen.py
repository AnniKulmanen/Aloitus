# SOVELLUS PAINOINDEKSIN JA KEHON RASVAPROSENTIN LASKEMISEEN
# ==========================================================

# Muuttujat
pituus = 172.0 # Pituus senttimetreinä (cm)
paino = 65.0 # Paino kilogrammoina (kg)

# Kaikki jotka ovat ''' ''' välissä muuttuivat kommenteiksi
'''
pituus_metreina = pituus / 100 

# Lasketaan painoindeksi (BMI)
bmi = paino / pituus_metreina **2

print('Painoindeksisi on', bmi)

'''
# Määritellään funktio painoindeksin laskentaan
def laske_bmi(paino, pituus):
    pituus = pituus / 100 # muutetaan pituus metreiksi
    bmi = paino / pituus**2
    return bmi 

bmi = laske_bmi(65, 172)

print('Painoindeksisi on edelleen', bmi)
