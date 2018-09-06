from django.urls import path
from .views import UserCreateAPIView
from rest_framework_jwt.views import obtain_jwt_token
from api.views import PlansList


urlpatterns = [
    path('login/', obtain_jwt_token, name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    # path('api/planList/', ListView.as_view(), name='api-list'),
    # path('api/mealTypeList/', MealTypeView.as_view(), name='api-TypeList'),
    path('plansList/', PlansList.as_view(), name='api-plan-List'),
    # path('api/snacksList/', SnacksList.as_view(), name='api-snack-List'),

]
