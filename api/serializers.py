from django.contrib.auth.models import User
from rest_framework import serializers
from .models import PlanList, MealTypeList, ListOfMeals, ListOfSnacks


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        return validated_data

class PlanListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanList
        fields = [
          'plan_type',
          'description'
            ]

class MealListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealTypeList
        fields = [
          'meal_type',
          'description'
            ]

class ListOfMealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListOfMeals
        fields = [
          'name', 
          'image',
          'Ingredients',
          'Instructions',
          'prep',
          'cook',
          'Ready_In',
          'Nutrition_Fac'
            ]

class ListOfSnacksSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListOfSnacks
        fields = [
          'name'
            ]


