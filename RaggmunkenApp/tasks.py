from celery import Celery

import foodnoticer
from models import FoodItem, User, AlertList
from Raggmunken.celery import app


@app.task()
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
    
