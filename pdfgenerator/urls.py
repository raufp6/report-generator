from django.urls import path
from .views import home,getPdfPage


app_name = "pdfgenerator"
urlpatterns = [
    path("",home,name="index"),
    path("pdf/",getPdfPage,name="index"),
]