from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import UserCreateSerializer, PlanListSerializer, MealListSerializer, ListOfMealsSerializer, ListOfSnacksSerializer
from .models import PlanList, MealTypeList, ListOfMeal, ListOfSnack

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class ListView(ListAPIView):
	queryset = PlanList.objects.all()
	serializer_class = PlanListSerializer

class MealTypeView(ListAPIView):
	queryset = MealTypeList.objects.all()
	serializer_class = MealListSerializer

class MealsList(ListAPIView):
	queryset = ListOfMeal.objects.all()
	serializer_class = ListOfMealsSerializer

class SnacksList(ListAPIView):
	queryset = ListOfSnack.objects.all()
	serializer_class = ListOfSnacksSerializer


