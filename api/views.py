from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import UserCreateSerializer, PlansSerializer
from .models import Plans

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class PlansList(ListAPIView):
	queryset = Plans.objects.all()
	serializer_class = PlansSerializer



