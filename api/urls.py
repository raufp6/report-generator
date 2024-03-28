from django.urls import path
from .views import api_home,MyTokenObtainPairView
from rest_framework_simplejwt.views import (
  
    TokenRefreshView,
)

app_name = "api"
urlpatterns = [
    path("",api_home,name="index"),
    path("token",MyTokenObtainPairView.as_view(),name="token_obtain_pair"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]