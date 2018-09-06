from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import UserCreateSerializer, PlansSerializer
from .models import Plans

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


# class ListView(ListAPIView):
# 	queryset = PlanList.objects.all()
# 	serializer_class = PlanListSerializer

# class MealTypeView(ListAPIView):
# 	queryset = MealTypeList.objects.all()
# 	serializer_class = MealListSerializer

class PlansList(ListAPIView):
	queryset = Plans.objects.all()
	serializer_class = PlansSerializer

# class SnacksList(ListAPIView):
# 	queryset = ListOfSnack.objects.all()
# 	serializer_class = ListOfSnacksSerializer


