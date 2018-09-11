from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import UserCreateSerializer, PlansSerializer, OrderSerializer

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import Plans, Order, OrderPlan

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class PlansList(ListAPIView):
	queryset = Plans.objects.all()
	serializer_class = PlansSerializer




class OrderCreation(APIView):
    # queryset = OrderPlan.objects.all()
    serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):
        # obj = Order.objects.create(user = request.user)
        # qty= OrderPlan.objects.get(qty = )
        order = Order.objects.create(user = request.user)
        data = request.data.get("obj")
        for order_plan in data:
            OrderPlan.objects.create(
                plan = Plans.objects.get(name= order_plan['name']),
                order= order,
                qty = order_plan['quantity']
            )
        return Response(status=  status.HTTP_201_CREATED)


class OrderList (ListAPIView):
    queryset = Order.objects.all()
    SerilizerMethodField = OrderPlan
    # queryset = Order.objects.all()
    serializer_class = OrderSerializer
    


       

















