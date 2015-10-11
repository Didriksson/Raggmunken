from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    
    def __unicode__(self):
        return '%s, %s' % (self.username,
                             self.email)

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
    
    
