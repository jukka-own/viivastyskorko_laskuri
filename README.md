# Viivästyskorkolaskuri

**Lyhyt kuvaus**

- viivästyskorot haetaan ja päivitetään [korkotutka](https://korkotutka.fi/viivastyskorko/) sivuilta
- laskee viivästyskoron annetulle summalle ja ajanjaksolle
- käyttää *kuluttajille* tarkoitettua viivästyskorkoa
- laskelman tulostus näytölle sekä pdf luonti

## Asennus
- luo virtuaalihakemiston koneellesi - `python -m venv nimiHakemistolle` <br>
- kopioi tiedostot hakemistoon
- aktivoi virtuaali ympäristö luomassasi hakemistossa - `Scripts\activate`
- asenna riippuvuudet - `pip install -r requirements.txt`

## Ohjelman käyttö
### korkoMain.py
Määritellään laskun maksamatton summa sekä laskun eräpäivä ja päivä jolloin maksu suoritettu. <br>
`korkoMain.py`  ohjelma käynnistelee funktiota alla olevissa ohjelmissa viivästyskoron laskemista varten.

### logWriter.py
Luo `log` tiedoston jos sitä ei vielä ole. 
Päivittää tiedostoa viivästyskorko datan ulkoisen haun osalta, kutsutaan useammasta eri ohjelmasta. <br>
Itse laskelmaa ei tallenneta. 

### updateNeeded.py
Tarkistaa `conf` tiedostosta milloin korko on viimeksi haettu. Jos korko jo haettu ja päivitetty kuluvan kuukauden aikana 
ei hakua tehdä toistamiseen. Jos `conf` tiedostoa ei vielä luotu luodaan se ja annetaan oletusarvot. 

### korkoHaku.py
Hakee korot [korkotutka](https://korkotutka.fi/viivastyskorko/) sivuilta. Tekee myös erinäisiä tarkistuksia että sivu on saavutettavissa
ja että sivun formaatti on pysynyt samana. Muokkaa sivulta haetun datan luettavampaan muotoon. 

### korkoTallennus.py
Ottaa varmuuskopion viimeksi luodusta tiedostosta ja tallentaa uudet korkoarvot `korot.csv` tiedostoon.

### fileToObj.py
Luo objektin tallennetun tiedoston pohjalta. 

### korkoLaskenta.py
Laskee myöhästymiskoron annetuilla päivämäärillä ja summalla.

### korkoTulostus.py
Muokkaa laskentun datan luettavampaan muotoon ja tulostaa sen ruudulle. 

### korkoPdf.py
Luo ja avaa käyttäjälle pdf tiedoston laskennasta.

### formatter.py
Muokkaa päivämääriä ja numeroita luettavampaan kuntoon.
