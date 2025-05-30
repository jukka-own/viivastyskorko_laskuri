import sys
from datetime import timedelta

# lasketaan korkokulut 6 kuukauden aikajaksoille 

def daysDelayed(ints, dueDate, paidDate, laskunSumma):
    
    delayed = (paidDate - dueDate).days                                 # montako päivää myöhässä 
    
    if delayed <= 0: 
        print("Ei vielä myöhästymiskorkoa")
        sys.exit(0)    
    else:         
        
        for self in ints:  
            if self.start <= paidDate <= self.end:                      # onko tämän kauden korko kyseessä, määrää koron
                if (paidDate - timedelta(delayed)) < self.start:        # jakautuuko useammalle kaudelle?
                    self.days = ((paidDate - self.start).days)          # monellekko päivällä korko lasketaan kauden sisällä 
                    self.sum = (((laskunSumma * ((self.int/100)+1))-laskunSumma)/365) * self.days 
                    delayed = (delayed - self.days)                    # seuraavan korkokauden päivät
                    paidDate = (self.start - timedelta(1))
               
                else:                                                   # tähän kun korko koko myöhästymisajan sama 
                    self.days = delayed
                    self.sum = (((laskunSumma * ((self.int/100)+1))-laskunSumma)/365)*delayed 
            