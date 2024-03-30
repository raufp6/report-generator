from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Report
from pdfgenerator.views import GeneratePdfPage
from datetime import datetime
import time
from .models import Report



@receiver(post_save, sender=Report)
def generate_pdf_on_report_creation(sender, instance, created, **kwargs):
    if created:
        all_data = {
            'logo':'',
            'timestamp':datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'),
            'client_name':instance.client_name,
            'physician_name':instance.physician_name,
            'patient_first_name':instance.patient_first_name,
            'patient_last_name':instance.patient_last_name,
            'patient_dob':instance.patient_dob,
            'patient_contact':instance.patient_contact,
            'chief_complaint':"It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)",
            'consultation_note':"It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)",
            'ip':""
        }
        GeneratePdfPage(all_data)