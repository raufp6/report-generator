from django.urls import path
from .views import home,GeneratePdfPage


app_name = "pdfgenerator"
urlpatterns = [
    path("",home,name="index"),
    path("pdf/",GeneratePdfPage,name="index"),
]