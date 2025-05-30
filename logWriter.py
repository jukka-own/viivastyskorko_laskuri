import os
from datetime import date, datetime

# päivittää logia

def logger(text):
    today = datetime.today().strftime('%d.%m.%Y')
    time = datetime.now().strftime("%H:%M:%S.%f") 
    time = time[:-3]
    wrapt = str(today) + ' ' + str(time) + ' '  + str(text)
    with open("log", "a", encoding="utf-8") as log:
        log.write(f'{wrapt}\n')  



