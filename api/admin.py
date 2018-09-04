from django.contrib import admin
from .models import  PlanList, MealTypeList, ListOfMeal, ListOfSnack 

admin.site.register(PlanList)
admin.site.register(MealTypeList)
admin.site.register(ListOfMeal)
admin.site.register(ListOfSnack)


