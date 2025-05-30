from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
import subprocess
from datetime import datetime
from formatter import *
import pathlib 
import os

# pdf tiedosto koroista

def pdfCreator(korkoObj, laskunSumma, due, paid):
 
    time = datetime.now().strftime("%H%M%S") 
    fileName = r'korot' + r"{}".format(time) + r'.pdf'
    
    p = pathlib.Path().resolve() / pathlib.Path("pdf/") 
    pathlib.Path(p).mkdir(exist_ok=True)                                    # jos hakemistoa ei ole 
    fullPath = os.path.join(p, fileName) 

    documentTitle = 'Viivästyskorko'
    title = 'Viivästyskorko'
 
    a = ' ' * 10
    subTitle = 'Kausi' + a + a + 'Päivät' + '   %' + '      €'
    
    pdf = canvas.Canvas(fullPath)
     
    # setting the title of the document
    pdf.setTitle(documentTitle)
    pdf.drawCentredString(300, 770, title)

    # creating the subtitle by setting it's font, 
    # colour and putting it on the canvas
    pdf.setFillColorRGB(0, 0, 255)
    pdf.setFont("Courier-Bold", 12)
    pdf.drawString(29, 720, subTitle)

    # drawing a line
    pdf.line(30, 710, 550, 710)

    # creating a multiline text using
    # textline and for loop
    text = pdf.beginText(40, 680) 
    text.setFont("Courier", 12)
    text.setFillColor(colors.red)

    for o in korkoObj:
        if o.days > 0:
            
            em, sm, sd, d, i, s = reFormat(o)                       # formatoidaan parempaan muotoon
        
            text.textLine(sd + '.' + sm + '.' + str(o.start.year) + ' - ' \
            + str(o.end.day) + '.' + em + '.' + str(o.end.year) + '   ' + d + '   ' + i + '   ' + s)
             
 
    text.textLine("")
    text.textLine("") 
    s1 = round(sum(self.sum  for self in korkoObj),2)               # 2 decimaalia summa
    s2 = sum(self.days  for self in korkoObj)                       # paivat
    text.textLine('Alkuperäinen velkasumma : ' + str(laskunSumma) + '€') 
    text.textLine('Myöhästyneitä päiviä    : ' + str(s2))
    text.textLine('Korkoa kertyi           : ' + str(s1) + '€')
    text.textLine("")
    text.textLine("") 
    text.textLine("Alkuperäinen eräpäivä   : " + dateFormat(due))
    text.textLine("Maksun päivämäärä       : " +  dateFormat(paid)) 
    

    if (s1 == s2) and (s1 == 0):
        text.textLine('')
        text.textLine('Korkoa ei pystytty laskemaan')
        text.textLine('Mahdollinen syy:') 
        text.textLine('Maksettu -päivämäärä on suurempi kuin uusimman korkokauden päättys pvm')
        text.textLine('Tarkista Maksettu -päivämäärä, korot.csv, sekä logi tiedosto')        

    pdf.drawText(text) 

    # save & open the pdf
    pdf.save()
    subprocess.Popen([fullPath], shell=True)
 