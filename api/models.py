from django.db import models
from django.contrib.auth.models import User



class Plans(models.Model):
	name = models.CharField(max_length= 250)
	image = models.ImageField(default='image')
	description = models.CharField(max_length= 1000, default="")
	
	totalPrice = models.DecimalField(decimal_places = 2, max_digits=5)


	def __str__(self):
		return self.name


# for plans ...... orderplan is the table connecting plans and order

class Order(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE, null= True)
	plans = models.ManyToManyField(Plans, through ='OrderPlan')
	date_time = models.DateTimeField(auto_now_add = True, auto_now= False)

	# def __str__(self):
	# 	return self.date_time


class OrderPlan(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	qty = models.IntegerField(default=0, null= True)
	price = models.DecimalField(default = 0, decimal_places = 2, max_digits=5)
	plan = models.ForeignKey(Plans, on_delete=models.CASCADE)

	def __str__(self):
		return self.plan


# FOR Profile

class Profile(models.Model):
	user_name = models.OneToOneField(User, on_delete = models.CASCADE)
	birth_date = models.DateField(null=True, blank=True)
	country = models.CharField(max_length=40, blank=True)
	phone = models.CharField(max_length=20, blank=True, default='')

	def __str__(self):
		return self.user_name