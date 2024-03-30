from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework import viewsets

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.generics import  ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from .serializers import MyTokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import HttpResponse


from pdfgenerator.serializers import ReportSerializer
from pdfgenerator.models import Report

from pdfgenerator.views import GeneratePdfPage
import time
from datetime import datetime
from xhtml2pdf import pisa

import os


@api_view(["GET"])
def api_home(request,*args, **kwargs):
    return Response({"message":"Hello world"})

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class LogoutView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'detail': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': 'Invalid refresh token.'}, status=status.HTTP_400_BAD_REQUEST)
        
class GeneratePDFView(APIView):
    def get(self, request):
        # Create a response object
        all_data = {
            'logo':'',
            'timestamp':datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'),
            'client_name':"Clicks Eon",
            'physician_name':"Dr.Kiran",
            'patient_first_name':'Arif',
            'patient_last_name':'bur',
            'patient_dob':'12-02-1994',
            'patient_contact':'+91 8606058722',
            'chief_complaint':"It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)",
            'consultation_note':"It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)",
            'ip':""
        }
        if GeneratePdfPage(all_data):
            return Response({"message":"Hello world"})
        
        return Response({"message":"error"})
    


    



class ReportCreateAPIView(APIView):
    def get(self, request, format=None):
        reports = Report.objects.all()
        serializer = ReportSerializer(reports, many=True)
        return Response(serializer.data)
    
    
    def post(self, request, format=None):
        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(added_by=request.user)  # Set the added_by field to the current user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        




        
