# GET BASIC INFORMATION ABOUT AN ATHLETE AND REATE ATHLETE OBJECTS
# ----------------------------------------------------------------

# LIBRARIES AND MODULES

import kuntoilija
import questions


# Ask a question and convert the answer to float






# Enter information about an athlete
name = input('Nimi: ')

# Ask details about her/him
question = questions.Question('Kuinka paljon painat (kg): ')
weight = question.ask_user_float(True)[0]
question =questions.Question('Kuinka pitkä olet (cm): ')
height = question.ask_user_float(True)[0]
question = questions.Question('Kuinka vanha olet: ')
age = question.ask_user_integer(True)[0]
question = questions.Question('Sukupuoli 1 mies, 0 nainen: ')
gender = question.ask_user_integer(True)[0]
question = questions.Question('Mikä on kaulanympäryksesi (cm): ')
neck = question.ask_user_float(True)[0]
question = questions.Question('Mikä on vyötärönympäryksesi (cm): ')
waist = question.ask_user_float(True)[0]
if gender == 0:
    question = questions.Question('Mikä on lantionympäryksesi (cm): ')
    hips = question.ask_user_float(True)[0]

# Create an athlete object from Kuntoilija class
athlete = kuntoilija.Kuntoilija(name, height, weight, age, gender)

# Print some information about the athlete
text_to_show = f'Terve {athlete.nimi}, painoindeksisi on tänään {athlete.bmi}'
print(text_to_show)
fat_percentage = athlete.rasvaprosentti()
if gender == 1:
    use_fat_percentage = athlete.usa_rasvaprosentti_mies(height, waist, neck)
else:
    use_fat_percentage = athlete.usa_rasvaprosentti_nainen(height, waist, neck, hips)

def ask_user(question):
    """Ask a question from the user and converts answer to a floating point number

    Args:
        question (str): The question to ask

    Returns:
        tuple: answer as float, Error message, Error Code and a detailed error message
    """
    while True:
        answer_txt = input(question)

        # Let's try to convert input to numeric
        try:
            answer = float(answer_txt)
            result = (answer, 'OK', 0, 'Conversion successful')
            break
    # If an error occurs tell the user to check
        except Exception as e:
            print('Virhe syötetyssä arvossa, älä käytä yksiköitä', e)
            result = (0, 'Error', 1, str(e))
    return result


# Enter information about an athlete
nimi = input('Nimi: ')

# Use ask_user function to get height and convert it into float
answer = ask_user('Pituus (cm) ')

# Read the 1st element of the tuple containing height value
pituus = answer[0]

answer = ask_user('Paino (kg) ')
paino = answer[0]

answer = ask_user('Ikä')
ika = answer[0]

answer = ask_user('Sukupuoli 0-nainen, 1-mies) ')
sukupuoli = answer[0]


'''
# Loop until user gives a correctly formatted value to height question
while True:
    pituus_txt = input('Pituus (cm): ')

    # Let's try to convert input to numeric
    try:
        pituus = float(pituus_txt)
        break
    #If an error occurs tell the user to check
    except Exception as e:
        print('Virhe syötetyssä arvossa, älä käytä yksiköitä', e)

# Loop until correct weight value
while True:
    paino_txt = input('Paino (kg): ')

# Let's try to convert input to numeric
    try:
        paino = float(paino_txt)
        break
    #If an error occurs tell the user to check
    except Exception as e:
        print('Virhe syötetyssä arvossa, älä käytä yksiköitä', e)

# Loop until correct age value
while True:
    ika_txt = input('Ikä: ')

# Let's try to convert input to numeric
    try:
        ika = float(ika_txt)
        break
    #If an error occurs tell the user to check
    except Exception as e:
        print('Virhe syötetyssä arvossa, älä käytä yksiköitä', e)

# Loop until correct gander value
while True:
    sukupuoli_txt = input('Sukupuoli, 1 mies, 0 nainen: ')

# Let's try to convert input to numeric
    try:
        sukupuoli = float(sukupuoli_txt)
        break
    #If an error occurs tell the user to check
    except Exception as e:
        print('Virhe syötetyssä arvossa, vain 1 ja 0 sallittu', e)

    '''
kuntoilija1 = kuntoilija.Kuntoilija(nimi, pituus, paino, ika, sukupuoli)

print(kuntoilija1.nimi, 'painoindeksisi on ', kuntoilija1.bmi)

print('Viimeisen kysymyksen virheilmoitus',
      answer[1], 'koodi', answer[2], 'engl. ilmoitus', answer[3])