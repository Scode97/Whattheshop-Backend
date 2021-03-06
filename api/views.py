from rest_framework.generics import CreateAPIView, ListAPIView,  DestroyAPIView
from .serializers import UserCreateSerializer, PlansSerializer, OrderSerializer, ProfileSerializer, OrderPlanListSerializer

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import Plans, Order, OrderPlan, Profile

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class PlansList(ListAPIView):
	queryset = Plans.objects.all()
	serializer_class = PlansSerializer


class ProfileAPIView(CreateAPIView):
    serializer_class = ProfileSerializer


class ProfileList(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class DeleteProfileAPIView(DestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'profile_id'

class DeleteAPIView(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'order_id'







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


# class OrderList (ListAPIView):


class OrderList(APIView):
    
 

    def get(self, request, *args, **kwargs):
        user_orders = Order.objects.filter(user= kwargs.get('user_id'))

        serializer = OrderSerializer(user_orders, many= True)
        return Response(serializer.data, status=status.HTTP_200_OK)


   

















