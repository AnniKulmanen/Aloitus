# PÄÄLUOKKA 

# KUNTOILIJAN TIEDOT OLIO-OHJELMOINTINA
# =====================================

# KIRJASTOT AJ MODUULIT (LIBRARIES AND MODULES)
# ---------------------------------------------

import fitness

# LUOKKAMÄÄRITYKSET (CLASS DEFINITIONS)
# -------------------------------------


# Kuntoilija-luokka Yliluokka (super class) JuniorKuntoilijalle 

# Luokan nimi alkaa aina ISOLLA kirjaimella ja olio alkaa pienellä esim. Kuntoilija ja kuntoilija
class Kuntoilija:
    """Luokka kuntoilijan tietoja varten"""

    # Oliomuodostin eli konstruktori, self -> tuleva olio (jonka nimeä ei vielä tiedetä) mutta sen parametrit laitetaan tähän
    def __init__(self, nimi, pituus, paino, ika, sukupuoli):
        
        # Määritellään tulevan olion ominaisuudet (property), luokan kentät (field)
        self.nimi = nimi
        self.pituus = pituus 
        self.paino = paino
        self.ika = ika
        self.sukupuoli = sukupuoli
        self.bmi = fitness.laske_bmi(self.paino, self.pituus)

    # Metodi rasvaprosentin laskemiseen (yleinen/aikuinen)
    def rasvaprosentti(self): # Tähän voisi laittaa parametreja jos haluaa
        self.rasvaprosenntti = fitness.aikuisen_rasvaprosentti(self.bmi, self.ika, self.sukupuoli) # Tässä haetaan fitness.py tietoja kun laitat vain fitness. sinulle ehdotetaan tietoja joita sieltä on saatavilla ja kun laitat sulut loppuun se kertoo mitä tarvitset. Koska meillä oli tehty self.bmi,self,ika jne oliot voit käyttää niitä tässä
        return self.rasvaprosenntti  # Kun kutsutaan kuntoilija oliosta rasvaprosenttia. Tähän ptäisi tulla rasvaprosentti
    
# JuniorKuntoilija-luokka Kuntoilija-luokan ailuokka (subclass)


class JunioriKuntoilija(Kuntoilija):
    """Luokka nuoren kuntoilijan tiedoille """

    # Konstruktori
    def __init__(self, nimi, pituus, paino, ika, sukupuoli):

        # Määritellään periytyminen, mitä ominaisuuksia perii
        super().__init__(nimi, pituus, paino, ika, sukupuoli) 

    # Metodi rasvaprosentin laskemiseen (ylikirjoitettu lapsen metodilla)
    def rasvaprosentti(self): 
        self.rasvaprosentti = fitness.lapsen_rasvaprosentti(self.bmi, self.ika, self.sukupuoli) 
        return self.rasvaprosentti 

    

if __name__ == '__main__': # Kaikki tämän yläpuolella on käytettävissä muualla mutta alapuolella olevat ei. (alapuolella olevaa koodia ei suoriteta)

    # Luodaan oli luokasta Kuntoilija
    kuntoilija = Kuntoilija('Kalle Kuntoilija', 171, 65, 40, 1)
    print(kuntoilija.nimi, 'painaa', kuntoilija.paino, 'kg')
    #print('painoindeksi on', kuntoilija.bmi)
    print('rasvaprosentti on ', kuntoilija.rasvaprosentti ())

    juniorkuntoilija = JunioriKuntoilija('Aku', 171, 65, 16, 1)
    print(juniorkuntoilija.nimi, 'painaa', juniorkuntoilija.paino, 'kg')
    #print('painoindeksi on', kuntoilija.bmi)
    print('rasvaprosentti on ', juniorkuntoilija.rasvaprosentti ())
    
