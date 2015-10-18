#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

import yagmail


"""
Den här lösningen fungerar ENDAST i unixmiljö.
"""
def sendNotice(fooditem):
    yag = yagmail.SMTP('didrikssonfoodmonitor@gmail.com')
    to = fooditem.username.email.encode('utf8')
    subject = u'Food alert! Kasta matlådan!'.encode('utf8')
    body = u'Godmorgon!\n Imorgon serveras inget mindre än '.encode('utf8') + fooditem.food.encode('utf8') + u' på Kompassen. Väl mött!\n Hälsningar,\nDidriksson Food Monitor'.encode('utf8')
    yag.send(to=to, subject=subject, contents=[body])
