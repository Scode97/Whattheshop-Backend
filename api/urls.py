from django.urls import path
from .views import UserCreateAPIView, DeleteProfileAPIView, ProfileAPIView,  ProfileList
from rest_framework_jwt.views import obtain_jwt_token
from api.views import PlansList, OrderCreation, OrderList


urlpatterns = [
    path('login/', obtain_jwt_token, name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),

    path('profilelist/', ProfileList.as_view(), name='api-profile-List'),

    path('createprofile/', ProfileAPIView.as_view(), name='api-create'),
    path('deleteprofile/<int:profile_id>/', DeleteProfileAPIView.as_view(), name='api-delete'),


    path('plansList/', PlansList.as_view(), name='api-plan-List'),

    path('orders/', OrderCreation.as_view(), name = 'api-orders'),
    path('orderlist/', OrderList.as_view(), name = 'api-order-list'),

]
