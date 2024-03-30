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

from fpdf import FPDF
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
        



def report(request):
    sales = [
        {"item": "Abdul", "amount": "$120,00"},
        {"item": "Mouse", "amount": "$10,00"},
        {"item": "House", "amount": "$1 000 000,00"},
    ]
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_font('courier', '', 12)

    for line in sales:
        pdf.cell(200, 8, f"Name : {line['item'].ljust(30)} {line['amount'].rjust(20)}", 0, 1)

    pdf.set_font('courier', '', 10)
    pdf.multi_cell(180, 10, 'This is what you have sold this month so far:This is what you have sold this month so far:This is what you have sold this month so far:This is what you have sold this month so far:This is what you have sold this month so far:This is what you have sold this month so far:This is what you have sold this month so far:',0,'J')
    # pdf.cell(40, 10, '',0,1)
    
    pdf.cell(200, 8, f"{'Item'.ljust(30)} {'Amount'.rjust(20)}", 0, 1)
    # pdf.line(10, 30, 150, 30)
    # pdf.line(10, 38, 150, 38)
    

    pdf.output('tuto1.pdf', 'F')
    return HttpResponse("ssasas")

def generate_pdf(request):
    # Load RML template
    current_dir = os.path.dirname(os.path.abspath(__file__))

    data = [
        {"client_name": "Keyboard"},
        {'contant':"contant"}
    ]
    
    template_path = os.path.join(current_dir, 'invoice_template.html')
    pdf_path = os.path.join(current_dir, 'invoice.pdf')

    with open(template_path, 'r') as template_file:
        template_content = template_file.read()
    
    # # Render RML to PDF
    # with open(pdf_path, 'wb') as pdf_file:
    #     pisa.CreatePDF(template_content, dest=pdf_file)

    # Render RML to PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'
    pisa_status = pisa.CreatePDF(template_content, dest=response)
    if pisa_status.err:
        return HttpResponse('Error rendering PDF', status=500)
    return response
        
