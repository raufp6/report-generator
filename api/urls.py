from django.urls import path
from .views import api_home,MyTokenObtainPairView,LogoutView,GeneratePDFView,ReportCreateAPIView
from rest_framework_simplejwt.views import (
  
    TokenRefreshView,
)

app_name = "api"
urlpatterns = [
    path("",api_home,name="index"),
    path("token/",MyTokenObtainPairView.as_view(),name="token_obtain_pair"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('generate_pdf/', GeneratePDFView.as_view(), name='generate_pdf'),
    path('report/', ReportCreateAPIView.as_view(), name='report'),
    path('save_report/', ReportCreateAPIView.as_view(), name='save_report'),


]