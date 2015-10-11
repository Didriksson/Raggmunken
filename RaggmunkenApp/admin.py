from django.contrib import admin

from .models import User, FoodItem, AlertList


# Register your models here.
admin.site.register(FoodItem)
admin.site.register(User)
admin.site.register(AlertList)