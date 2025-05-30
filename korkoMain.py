from korkoHaku import *
from korkoTallennus import *
from cCreator import *
from fileToObj import *
from korkoLaskenta import * 
from korkoTulostus import *
from logWriter import *
from updateNeeded import * 
from korkoPdf import * 
import os 
 

fName = "korot.csv"
os.system('cls')                                                             

# input
laskunSumma = 99.99
orgDueDate = date(2024,12,29) 
dueDate = orgDueDate + timedelta(1)                                         # laskenta alkaa eräpäivän jälkeisestä päivästä 
paidDate = date(2025,3,1)  

logger("*" * 101)                                                           # logWriter
logger("Ohjelma käynnistetty (" + os.path.basename(__file__) + ")")         


last =  checker("check") 
if last != False:                                                           # updatedNeeded - onko data vielä ajankohtaista    
    interests = fetchInterest()                                             # korkoHaku - korot haetaan netistä 
    if interests != False:
        trueUpdate = fileInterests(interests,fName,last)                    # KorkotTallennus - tiedosto luodaan
        if trueUpdate:                                                      # onko verkkosivun data päivittynyt 
            checker("update")                                               # updatedNeeded - ajopäivät päivitetään conf tiedostoon
        else:
            logger("Verkkosivujen data ei ole vielä päivittynyt. " 
              "Seuraavalla ajokerralla uusi yritys. ")                                                                 
    else:
        print("Laskelma tehty mahdollisesti vanhentuneilla tiedoilla")
        logger("Laskelma tehty mahdollisesti vanhentuneilla tiedoilla")

allObjects = oCreator(fName)                                                # fileToObj - objektit luodaan tiedoston datasta

daysDelayed(allObjects, dueDate, paidDate, laskunSumma)                     # korkoLaskenta - lasketaan viivästyskorko
 
tulostus(allObjects, laskunSumma, orgDueDate, paidDate)                     # korkoTulostus

pdfCreator(allObjects, laskunSumma, orgDueDate, paidDate)                   # korkoPdf - luodaan pdf tiedosto