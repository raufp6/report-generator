from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework import viewsets

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.generics import  ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import MyTokenObtainPairSerializer


@api_view(["GET"])
def api_home(request,*args, **kwargs):
    return Response({"message":"Hello world"})


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
