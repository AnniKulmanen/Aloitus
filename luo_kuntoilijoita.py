# GET BASIC INFORMATION ABOUT AN ATHLETE AND REATE ATHLETE OBJECTS
# ----------------------------------------------------------------

# LIBRARIES AND MODULES     # EI tässä mutta yleisesti näin voi tehdä ei pakko    
import json                 # 1. Pythonin ulkoiset moduulit
import kuntoilija           # 2. Pythonin sisäiset moduulit  
import questions            # 3. Oma tekemät moduulit


# Ask a question and convert the answer to float


# Enter information about an athlete
name = input('Nimi: ')
date_of_weighing = input('Punnituspäivä (vvvv-kk-pp): ')

# Ask details about her/him

weight = questions.Question.ask_user_float('Kuinka paljon painat (kg): ', True)[0]
height = questions.Question.ask_user_float('Kuinka pitkä olet (cm): ', True)[0]
age = questions.Question.ask_user_integer('Kuinka vanha olet: ', True)[0]
allowed_genders = {'1': 1, '0': 0}  # Palauttaa kokonaisluvun 1 tai 0. Muuttaa tekstin numeroksi.
gender = questions.Question.ask_user_dictionary('Sukupuoli 1 mies, 0 nainen: ', allowed_genders, True)[0]   # True takia kysyy kysymystä niin kauan että vastaa 1 tai 0
neck = questions.Question.ask_user_float('Mikä on kaulanympäryksesi (cm): ', True)[0]
waist = questions.Question.ask_user_float('Mikä on vyötärönympäryksesi: ', True)[0]

# If woman ask circumference of her hips
if gender == 0: 
    hips = questions.Question.ask_user_float('Mikä on lantionympäryksesi: ', True)[0]

# Create an athlete object from Kuntoilija class
athlete = kuntoilija.Kuntoilija(name, height, weight, age, gender, date_of_weighing)

# Print some information about the athlete
text_to_show = f'Terve {athlete.nimi}, painoindeksisi on tänään {athlete.bmi}'
print(text_to_show)
fat_percentage = athlete.rasvaprosentti()

# If male use usa_rasvaprosentti_mies method
if gender == 1:
    usa_fat_percentage = athlete.usa_rasvaprosentti_mies(height, waist, neck)
else:
    usa_fat_percentage = athlete.usa_rasvaprosentti_nainen(height, waist, hips, neck)

text_to_show = f'suomalainen rasva-% on {fat_percentage} ja amerikkalainen on {usa_fat_percentage}'
print(text_to_show)

print('Nimi', athlete.nimi, 'paino', athlete.paino)

# athlete_data = [] # Empty list for all athlete data

# Read previous athlete_data from disk
with open('athlete_data.json', 'r') as file:
    athlete_data = json.load(file)          # Silloin kun tiedosto avataan, json muutetaan uudestaan sanakirjaksi nimeltään athlete_data
    for item in athlete_data:               # Luetaan silmukassa läpi. athlete_data on lista eli siellä on jotakin jota voidaan toistaa. item on keksitty. Se on yksittäinen asia listassa jota kutsutaan
        print('paino oli', item['paino'])   # paino oli ja haetaan sanakirjasta paino. Esim. paino oli 60

# A dictionary for single weighing of an athlete
athlete_data_row = {'nimi': athlete.nimi, 'pituus': athlete.pituus, 'paino': athlete.paino, 
                    'ika': athlete.ika, 'sukupuoli': athlete.sukupuoli, 'pvm': athlete.punnitus_paiva}

# Add a new data row to the athlete_data list
athlete_data.append(athlete_data_row)

# SAVE DATA TO A FILE

with open('athlete_data.json', 'w') as file: # luo athlete_data.json objektin. w koska halutaan kirjoittaa json.
    json.dump(athlete_data, file, indent=4) # Haetaan json kirjastosta dump. dump haluaa objektin ja fp eli tiedoston. 
                                            # Jos haluaa AINA vikaksi voi laittaa indent=4 eli 4 välin sisennys (sisentää tekstin helpommin luettavaksi)
                                            # Sen jälkeen tallenna ja aja terminaali


