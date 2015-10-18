#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

"""
Den h�r l�sningen fungerar ENDAST i unixmilj�.
"""

import yagmail, emaildetails, base64


def sendNotice(fooditem):
    yag = yagmail.SMTP(emaildetails.emailaddress, base64.standard_b64decode(emaildetails.key))
    to = fooditem.username.email.encode('utf8')
    subject = u'Food alert! Kasta matl�dan!'.encode('utf8')
    body = u'Godmorgon!\n Imorgon serveras inget mindre �n '.encode('utf8') + fooditem.food.encode('utf8') + u' p� Kompassen. V�l m�tt!\n H�lsningar,\nDidriksson Food Monitor'.encode('utf8')
    yag.send(to=to, subject=subject, contents=[body])
