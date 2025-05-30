import os
import shutil
from logWriter import *
from formatter import *
# Tallennetaan haetut korot csv muotoon

def fileInterests(data,fName, last):
    if os.path.exists(fName):
        opt = "w"
        logger("Vanha korkotiedosto tallennettu backup_ nimellä (" + os.path.basename(__file__) + ")")
        shutil.copyfile(fName,'backup_'+fName)
    else:
        opt = "a"

    f = open(fName,opt)
    newD = []
    trueUpdate = False
    for d in data:
        if len(d) > 8:
            newD = (d.split('.')) 
            f.write(newD[4] + ',' + newD[1] + ',' + newD[0] + ',' + newD[4] + ',' + newD[3] + ',' + newD[2] + ',')
            if monthFormat(newD[4],newD[3]) > int(last):
                trueUpdate = True
        else:            
            f.write(d + '\n')
    
    logger("Uusi korkotiedosto tallennettu nimellä " + fName + " (" + os.path.basename(__file__) + ")")
    logger("Tallennus suorittettu")
    
    return trueUpdate  