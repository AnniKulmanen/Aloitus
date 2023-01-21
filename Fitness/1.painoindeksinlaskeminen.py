# SOVELLUS PAINOINDEKSIN JA KEHON RASVAPROSENTIN LASKEMISEEN
# ==========================================================

# Muuttujat
pituus = 172.0 # Pituus senttimetreinä (cm)
paino = 65.0 # Paino kilogrammoina (kg)

pituus_metreina = pituus / 100

# Lasketaan painoindeksi (BMI)
bmi = paino / pituus_metreina **2

print('Painoindeksisi on', bmi)