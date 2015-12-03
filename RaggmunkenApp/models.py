from django.contrib.auth.models import User
from django.db import models


class FoodItem(models.Model):
    username = models.ForeignKey(User)
    food = models.CharField(max_length=200)
    def __unicode__(self):
        return self.username.__unicode__() + " - " + self.food
        
class AlertList(models.Model):
    fooditem = models.ForeignKey(FoodItem)
    servingdate = models.CharField(max_length=200)
    def __unicode__(self):
        return self.fooditem.__unicode__() + " - " + self.servingdate
    