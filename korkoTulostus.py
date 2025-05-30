import sys
from formatter import *

# yhteenveto tulostus ruudulle

def tulostus(allObjects, laskunSumma, orgDueDate, paidDate):

    print("| %-23s | %-6s  | %-7s | %-8s" % ("Kausi".center(23), "Päivät", "%".center(7), "€".center(16)))
  
    for self in allObjects:
        if self.sum != 0:
            print(self) 

    print("\nAlkuperäinen velkasumma: ", laskunSumma,  
    "€\nKorkoa kertyi: ", round(sum(self.sum  for self in allObjects),2), 
    "€\nMyöhästyneitä päiviä: ", sum(self.days  for self in allObjects),
    "\nEräpivä: ", dateFormat(orgDueDate),
    "\nMaksettu:",dateFormat(paidDate))
 

