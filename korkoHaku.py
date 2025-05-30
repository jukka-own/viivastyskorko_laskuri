# hakee korot sivulta 

from urllib.request import urlopen
import re
import requests
from bs4 import BeautifulSoup
from logWriter import *

def fetchInterest():
       
    url = "https://korkotutka.fi/viivastyskorko/"

    logger("Tarkistetaan että sivusto pystyssä " + url + " (" + os.path.basename(__file__) + ")")

    r = requests.head(url)
    if r.status_code == 200:
        logger("Sivusto pystyssä, korkoja lähdetään hakemaan " + url + " (" + os.path.basename(__file__) + ")")
    else:
        logger("Korkoja ei pystytä hakemaan " + url + " (" + os.path.basename(__file__) + ")")
        logger("Korkoja ei päivitetä ja ohjelma suoritetaan jo olemassa olevilla koroilla " + url + " (" + os.path.basename(__file__) + ")")
        return False

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    
    stripString = "%\n -"
    all = []

    if soup.find_all("td", {"class": "column-1"}):   

        for EachPart in soup.select('tr[class*="row-"]'): 
            if EachPart.get("class") == ['row-1']:
                continue
            else: 
                fAll = EachPart.find_all("td" , recursive=False)
                for f in fAll: 
                    if f.get("class") == ['column-3']:
                        continue
                    else: 
                        t = re.sub("[" + stripString + "]", "", f.get_text())
                        t = t.replace(',','.')
                        all.append(t)
    else:
        logger("Korkoja ei pystytä hakemaan " + url + " (" + os.path.basename(__file__) + ")")
        logger("Sivusto toimi mutta haluttua taulukkoa ei löytynyt " + url + " (" + os.path.basename(__file__) + ")")
        return False

    logger("Korot haettu sivulta " + url + " (" + os.path.basename(__file__) + ")")    
    return(all) 