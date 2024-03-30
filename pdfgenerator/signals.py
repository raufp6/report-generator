from django.db.models.signals import post_save
from django.dispatch import receiver
from pdfgenerator.views import GeneratePdfPage
from datetime import datetime
import time
from .models import Report

@receiver(post_save, sender=Report)
def generate_pdf_on_report_creation(sender, instance, created, **kwargs):
    if created:
        all_data = {
            'logo':instance.logo,
            'timestamp':datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'),
            'client_name':instance.client_name,
            'physician_name':instance.physician_name,
            'patient_first_name':instance.patient_first_name,
            'patient_last_name':instance.patient_last_name,
            'patient_dob':instance.patient_dob,
            'patient_contact':instance.patient_contact,
            'chief_complaint':instance.chief_complaint,
            'consultation_note':instance.consultation_note,
        }
        response = GeneratePdfPage(all_data)

        # Update generated file name 
        instance.report_pdf_file = response
        instance.save()