from django.urls import path
from .views import UserCreateAPIView
from rest_framework_jwt.views import obtain_jwt_token
from api.views import PlansList, OrderCreation, OrderList


urlpatterns = [
    path('login/', obtain_jwt_token, name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),

    path('plansList/', PlansList.as_view(), name='api-plan-List'),

    path('orders/', OrderCreation.as_view(), name = 'api-orders'),
    path('orderlist/', OrderList.as_view(), name = 'api-order-list'),

]
