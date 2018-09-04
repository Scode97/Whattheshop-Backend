from django.db import models

class PlanList(models.Model):
	# name = models.CharField(max_length= 200)
	plan_type = models.CharField(max_length= 200)
	price = models.DecimalField(decimal_places = 2, max_digits=5)
	description = models.TextField()

	def __str__(self):
		return self.plan_type

class MealTypeList(models.Model):
	# name = models.CharField(max_length= 200)
	meal_type = models.CharField(max_length= 200)
	description = models.TextField()

	def __str__(self):
		return self.meal_type

class ListOfMeal(models.Model):
	name = models.CharField(max_length= 250)
	image = models.ImageField()
	Description = models.CharField(max_length= 1000, default="")
	Ingredients = models.TextField()
	Instructions = models.TextField()
	prep = models.CharField(max_length= 250, default="")
	cook = models.CharField(max_length= 250, default="")
	Ready_In= models.CharField(max_length= 250, default="")
	servings = models.CharField(max_length= 250, default="")
	Nutrition_Facts = models.TextField(default="")


	def __str__(self):
		return self.name

class ListOfSnack(models.Model):
	name = models.CharField(max_length= 250)

	def __str__(self):
		return self.name

