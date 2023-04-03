# Esimerkkejä päivämäärien, tiedostojen ja JSON-tiedostojen käytöstä

import datetime # Sisäänrakennettu kirjasto aikamääreille

# Päiväyksen muodostaminen

year = 2023
mont = 3
day = 17

date = datetime.datetime(year, mont, day)

print(date)

# Kuluvan päivän ja kellonajan selvittäminen
just_now = datetime.datetime.now()
print(just_now)



# Aika ero kahden päivämäärän välillä

# Funktio joka laskee päivämäärien eron päivinä
def datediff(d1, d2):  # muuttuja on datediff voi olla minkä niminen vain, sekä d1 ja d2 voi olla mitä vain
    """Calculates the  difference between two dates in days  (tämä on ohje mitä docstring tekee)

    Args:       # Tämä docstring
        d1 (str): A date in ISO format YYYY-MM-DD
        d2 (str): A date in ISO format YYYY-MM-DD

    Returns: 
        int: absolute difference in days  (Tämä on mitä docstring palauttaa)
    """
    d1 = datetime.datetime.strptime(d1, "%Y-%m-%d")  # eka pvä. Pitää olla 2 datetime eka on moduulista toka on tähä tarkotettu
    d2 = datetime.datetime.strptime(d2, "%Y-%m-%d")   # toka pvä
    difference = abs((d2 - d1).days)    # abs = jos menee negatiiviseksi abs muuttaa sen positiiviseksi. Muuttaa eron päiviksi. Voisi muuttaa myös vuosiksi, kuukausiksi
    return difference

ero = datediff('2023-03-17', '2023-01-20') # Tässä eka on d1 ja toka d2. Tässä annetaan d1, d2 bleeblee
print(ero)




# Funktio joka laskee kahden kellonajan välisen eron tunteina
def timediff(t1, t2):
    """Calculates the  difference between two time values  (tämä on ohje mitä docstring tekee)

    Args:
        t1 (str): time value in formnat HH:MM:SS
        t2 (str): time value in formnat HH:MM:SS

    Returns:
        float: time difference in hours  (Tämä on mitä docstring palauttaa)
    """
    t1 = datetime.datetime.strptime(t1, "%H:%M:%S")
    t2 = datetime.datetime.strptime(t2, "%H:%M:%S")
    seconds = abs((t2 - t1).seconds) # Vain sekunnit ja mikrosekunnit on tuettu timedeltassa
    hours = seconds / 3600
    return hours

kesto = timediff('10:00:00', '14:30:00')
print(kesto)