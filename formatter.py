# formatoi datan luettavampaan muotoon pdf:ää varten

def reFormat(o):
    if len(str(o.end.month)) == 1:
        em = '0' + str(o.end.month)
    else:
        em = str(o.end.month)

    if len(str(o.start.month)) == 1:
        sm = '0' + str(o.start.month)
    else:
        sm = str(o.start.month)

    if len(str(o.start.day)) == 1:
        sd = '0' + str(o.start.day)
    else:
        sd = str(o.start.day)
 
    if len(str(o.days)) == 1: 
        d ='  ' + str(o.days)         

    if len(str(o.days)) == 2:   
        d =' ' + str(o.days)
    
    if len(str(o.days)) == 3:
        d = str(o.days)

    if len(str(o.int)) == 3:
        i = ' ' + str(o.int)

    else:
        i = str(o.int)

    s = str(round(o.sum,4))
    
    return em, sm, sd, d, i, s

def dateFormat(d):                                      # ddmmyyyy
    return d.strftime("%d.%m.%Y")

def monthFormat(y,m):                                     # yyyymm - kuukauteen lisätään etunolla jos puuttuu
    if len(str(m)) == 1:
        m = '0' + m 
    return int(str(y+m))