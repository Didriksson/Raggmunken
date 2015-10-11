#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

from bs4 import BeautifulSoup
import urllib 


veckansMeny = {u'Måndag': [], "Tisdag" : [], "Onsdag": [], "Torsdag": [], "Fredag": []}
kompassen = "http://www.restaurangkompassen.se/index.php?option=com_content&view=article&id=64&Itemid=66"


def readMenu():
    nuvarandeVeckodag = 'Måndag'
    response = urllib.urlopen(kompassen)
    soup = BeautifulSoup(response.read(), 'html.parser')
    menyDivs = soup.findAll('div', attrs={'class':'meny_back'})
    for child in menyDivs[0].strings:
        if child in veckansMeny:
            nuvarandeVeckodag = child
        else:
            veckansMeny[nuvarandeVeckodag].append(child)


def findItemInMeny(item):
    for dag in veckansMeny:
        for mat in veckansMeny[dag]:
            if item.upper() in mat.upper():
                return dag
