from django.db import models
from django.contrib.auth.models import User



class Plans(models.Model):
	name = models.CharField(max_length= 250)
	image = models.ImageField(default='SOME STRING')
	description = models.CharField(max_length= 1000, default="")
	
	totalPrice = models.DecimalField(decimal_places = 2, max_digits=5)


	def __str__(self):
		return self.name


# FOR Profile

class Profile(models.Model):
	user_name = models.OneToOneField(User, on_delete = models.CASCADE)
	birth_date = models.DateField(null=True, blank=True)
	country = models.CharField(max_length=40, blank=True)
	phone = models.CharField(max_length=20, blank=True, default='')

	def __str__(self):
		return self.user_name


# class OrderPlan (models.Model):
# 	plans = models.CharField(plans, max_length = 250)
# 	order = models.CharField(order, max_length = 250)

# 	def __str__(self):
# 		return self.plans

# class Order (models.Model):
# 	user_name = models.ForeignKey(User, on_delete = models.CASCADE)
# 	plans = models.ManyToManyField(plans, through = OrderPlan)

# 	def __str__(self):
# 		return self.user_name






