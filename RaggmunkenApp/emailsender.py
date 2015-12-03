#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Den h�r l�sningen fungerar ENDAST i unixmilj�.
"""

import yagmail, emaildetails, base64

def sendNotice(fooditem):
    yag = yagmail.SMTP(emaildetails.emailaddress, base64.standard_b64decode(emaildetails.key))
    to = fooditem.username.email.encode('utf8')
    subject = 'Food alert! Kasta matlådan!'
    body = 'Godmorgon!\n Imorgon serveras inget mindre än ' + fooditem.food.encode("utf8") + ' på Kompassen. Väl mött!\n Hälsningar,\nDidriksson Food Monitor'
    yag.send(to=to, subject=subject, contents=[body])
    print 'Skickat mail!'


