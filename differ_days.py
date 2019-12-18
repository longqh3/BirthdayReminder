# -*- coding: UTF-8 -*-

import datetime

def date_part(date='20170301'):
    global year,month,day
    year=date[0:4]
    month_first=int(date[4:5])
    month = date[5:6]
    if month_first ==0:
        month = date[5:6]
    else :
        month = date[4:6]

    day=date[6:8]
    
    year = int(year)
    month = int(month)
    day = int(day)
    
    d = datetime.date(year,month,day)
    return d