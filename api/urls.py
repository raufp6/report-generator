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
    path('save_report/', ReportCreateAPIView.as_view(), name='save_report'),

    # path('report/', report, name='report'),
    # path('generate_pdf__/', generate_pdf, name='generate_pdf'),
    # path('gen_pdf_new/', GenerateReportView.as_view(), name='gen_pdf_new'),

]