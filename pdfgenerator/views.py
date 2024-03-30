from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa
from io import StringIO, BytesIO
import time
import os


def home(request):
    return HttpResponse("home")

def getPdfPage(request):
    
    all_data = {
        'logo':'',
        'timestamp':time.time(),
        'client_name':"Clicks Eon",
        'physician_name':"Dr.Kiran",
        'patient_first_name':'Fayis',
        'patient_last_name':'Rauf',
        'patient_dob':'12-02-1994',
        'patient_contact':'+91 8606058722',
        'chief_complaint':"It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)",
        'consultation_note':"It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)",
        'ip':""
    }
    data={'data':all_data}
    template=get_template("invoice_template.html")
    data_p=template.render(data)
    response=BytesIO()

    pdfPage = pisa.pisaDocument(BytesIO(data_p.encode("UTF-8")),response)
    
    current_dir = os.path.dirname(os.path.abspath(__file__))+"/reports/"
    file_name = f"CR_{all_data['patient_last_name']}_{all_data['patient_first_name']}_{all_data['patient_dob']}.pdf"

    pdf_path = os.path.join(current_dir, file_name)

    

    with open(pdf_path, 'wb') as pdf_file:
        pisa.CreatePDF(data_p, dest=pdf_file)
        
    if not pdfPage.err:
        return HttpResponse(response.getvalue(),content_type="application/pdf")
    else:
        return HttpResponse("Error Generating PDF")
