from django.db import models
from django.contrib.auth.models import User


class Report(models.Model):
    """ Report Model """
    added_by = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    client_name = models.CharField(max_length=100,default='Clinet name')    
    logo = models.FileField(upload_to='uploads/logos/') 
    physician_name = models.CharField(max_length=100,blank=True,null=True)
    physician_contact = models.CharField(max_length=15,blank=True,null=True)
    patient_first_name = models.CharField(max_length=100,null=True,blank=True)
    patient_last_name = models.CharField(max_length=100,null=True,blank=True)
    patient_dob = models.DateField(null=True,blank=True)
    patient_contact = models.CharField(max_length=15,null=True,blank=True)
    report_pdf_file = models.CharField(max_length=100,null=True,blank=True)
    chief_complaint = models.CharField(max_length=5000,null=True,blank=True)
    consultation_note = models.CharField(max_length=5000,null=True,blank=True)
    
    created_at = models.DateTimeField(null=True, blank=True,auto_now_add=True)
    deleted_at = models.DateField(null=True,blank=True)

    class Meta:
        verbose_name_plural = "Reports"
        ordering = ['-id']

    def __str__(self):
        return self.client_name