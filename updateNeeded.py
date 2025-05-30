# tarkistaa viimeksi ajetun päivän
# normaalisti korot päivitetään vuosittain kaksi kertaa
# 1.1 ja 1.7 
# tämä ohjelma käy kuitenkin kerran kuukaudessa tarkistamassa
# päivittää conf tiedostoa

import os
import datetime
from logWriter import *
from dateutil.relativedelta import relativedelta

def checker(checking):
    ym = datetime.now().strftime("%Y%m")
    if os.path.exists('conf') :
        file = open('conf') 
        content = file.readlines()
        last = content[0][-7:] 

    else:
        file = open('conf', 'a')                                        # aloitus arvot
        file.write('Last update:200001\n')
        file.write('Next update:200001') 
        last = 200001
        logger("conf - tiedosto luotu aloitus arvoilla(" + os.path.basename(__file__) + ")")

    if checking == "check":                                             # pvm tarkistus
        if int(last) < int(ym):                                         # viimeksi ajettu kuukausi pienempi kuin kuluva?
            logger("Korot tarkistettu ja tullaan päivittämään (" + os.path.basename(__file__) + ")" )
            # return True
            return last
        else:
            logger("Korkoja ei tarvitse vielä päivittää(" + os.path.basename(__file__) + ")")
            return False
    
    else:                                                               #pvm päivitys
        
        next = datetime.today() + relativedelta(months=1) 
        next = next.strftime("%Y%m")
        
        t1 = "Last update:" + str(ym) 
        t2 = "Next update:" + str(next)
        with open("conf", "w", encoding="utf-8") as conf:
            conf.write(f'{t1}\n')
            conf.write(f'{t2}\n')
            conf.write(f'File updated:{datetime.now()}\n')
        
        logger("conf - tiedosto päivitetty uusilla päivämäärillä")

        

 