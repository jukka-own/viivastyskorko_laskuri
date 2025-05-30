from cCreator import * 
import csv
from datetime import date 

def oCreator(fName):
    with open(fName, 'r') as csvfile:     
        allInter = []
        csv_read = csv.reader(csvfile, delimiter=',')
        for row in csv_read: 
            allInter.append(Interest({
                                    'start' :   date(int(row[0]),int(row[1]),int(row[2])),
                                    'end'   :   date(int(row[3]),int(row[4]),int(row[5])),
                                    'int'   :   float(row[6]),
                                    'days'  :   0,
                                    'sum'   :   0
                                    })
                            ) 
        return allInter