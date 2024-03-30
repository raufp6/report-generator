from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa
from io import BytesIO
import os


def home(request):
    return HttpResponse("home")

def GeneratePdfPage(all_data):
    """
    PDF Generate Function
    """
    
    # Form Data
    data={'data':all_data}
    template = get_template("report_template.html")
    rendered_data = template.render(data)
    response=BytesIO()

    pdfPage = pisa.pisaDocument(BytesIO(rendered_data.encode("UTF-8")),response)
   
    # Save PDF file
    current_dir = "uploads/reports/"
    file_name = f"CR_{all_data['patient_last_name']}_{all_data['patient_first_name']}_{all_data['patient_dob']}.pdf"
    pdf_path = os.path.join(current_dir, file_name)
    with open(pdf_path, 'wb') as pdf_file:
        pisa.CreatePDF(rendered_data, dest=pdf_file)
        
    if not pdfPage.err:
        return file_name
    else:
        return False
