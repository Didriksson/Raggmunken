#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

from celery.schedules import crontab
import datetime

from Raggmunken.celery import app
import emailsender
import foodnoticer
from models import FoodItem, User, AlertList


@app.task
def testingTask():
    print "Testing task, every minute."
    


@app.task
def sendTodaysEmails():
    dagar = {
            0 : u'M�ndag', 
            1 : 'Tisdag', 
            2 : 'Onsdag', 
            3 : 'Torsdag', 
            4 : 'Fredag', 
            5 : u'L�rdag', 
            6 : u'S�ndag'}
    
    
    """
    Vi k�r en klassisk mod f�r att kunna f� ut morgondagen / antal veckodagar.
    D.v.s. skulle s�ndag ploppa upp f�r vi S�ndag = 6 + 1 som �r en dag som inte finns.
    Men 7 % 7 ger oss 0 som �r M�ndag. Eureka! Efter att ha skickat iv�g ett mail
    till anv�ndaren tar vi bort raden ur databasen.
    """
    veckodag = dagar[(datetime.datetime.today().weekday()+1) % 7]
    for fooditem in AlertList.objects.filter(servingdate=veckodag):
        emailsender.sendNotice(fooditem.fooditem)
        AlertList.objects.get(fooditem=fooditem).delete()




@app.task
def performMenuCheck():
    userFoodList = {}
    for user in User.objects.all():
        for food in FoodItem.objects.filter(username=user):
            if user in userFoodList:
                userFoodList[user].append(food)
            else:
                userFoodList[user] = [food]
    
    print "Scanning menu..."
    foodnoticer.readMenu()


    for user in userFoodList:
        print "Trying To find menu item for user: " + user.username
        for food in userFoodList[user]:
            print "Trying to find a match for item: " + food.food
            dag =  foodnoticer.findItemInMeny(food.food)
            if dag:
                print "Found: " + dag
                AlertList.objects.create(fooditem=food, servingdate=dag)
    
