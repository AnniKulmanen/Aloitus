# FITNESS-MODUULIN TESTIT 
# =======================

# KIRJASTOJEN JA MODUULIEN LATAUKSET
import fitness

def test_laske_bmi():
    assert fitness.laske_bmi(64.7, 170) == 22.4
    assert fitness.laske_bmi(40, 170) == 13.8
    assert fitness.laske_bmi(100, 170) == 34.6

# Testejä aikuisia miehiä
def test_laske_aikuisen_rasvaprosentti():
    assert fitness.aikuisen_rasvaprosentti(22.4, 20, 1) == 15.3
    assert fitness.aikuisen_rasvaprosentti(13.8, 40, 1) == 9.6 
    assert fitness.aikuisen_rasvaprosentti(34.6, 70, 1) == 41.4

# Testejä aikuisia naisia
    assert fitness.aikuisen_rasvaprosentti(20.8, 20, 0) == 24.2
    assert fitness.aikuisen_rasvaprosentti(13.8, 40, 0) == 20.4
    assert fitness.aikuisen_rasvaprosentti(34.6, 60, 0) == 49.9
    
# Testejä lapset tyttö ja poika
def test_laske_lapsen_rasvaprosentti():
    assert fitness.lapsen_rasvaprosentti(24.4, 14, 0) == 28.4
    assert fitness.lapsen_rasvaprosentti(24.4, 14, 1) == 24.8
 
# Testejä USA:n rasvaprosentti laskurilla
def test_naisen_usa_rasvaprosentti():
    assert round(fitness.usarasvaprosentti_nainen(170, 70, 37, 90)) == 18
    assert round(fitness.usarasvaprosentti_nainen(170, 90, 42, 90)) == 26

def test_miehen_usa_rasvaprosentti():
    assert round(fitness.usarasvaprosentti_mies(171, 91, 38)) == 22
    assert round(fitness.usarasvaprosentti_mies(170, 120, 42)) == 37