from django.urls import path
from .views import MyTokenObtainPairView,LogoutView,ReportCreateAPIView
from rest_framework_simplejwt.views import (
  
    TokenRefreshView,
)

app_name = "api"
urlpatterns = [
    path("token/",MyTokenObtainPairView.as_view(),name="token_obtain_pair"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('report/', ReportCreateAPIView.as_view(), name='report'),
    path('save_report/', ReportCreateAPIView.as_view(), name='save_report'),
]