from django.contrib import admin
from .models import  PlanList, MealTypeList, ListOfMeals, ListOfSnacks 

admin.site.register(PlanList)
admin.site.register(MealTypeList)
admin.site.register(ListOfMeals)
admin.site.register(ListOfSnacks)


