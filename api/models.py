from django.db import models

class Reports(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
