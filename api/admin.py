from django.contrib import admin
from .models import Plans, Profile, OrderPlan, Order

admin.site.register(Plans)
admin.site.register(Profile)

admin.site.register(OrderPlan)
admin.site.register(Order)



