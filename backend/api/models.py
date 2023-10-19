# app_name/models.py
from django.db import models

class Application(models.Model):
    application_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)

    class Meta:
        app_label = 'api'

class Compliance(models.Model):
    name = models.CharField(max_length=100)
    applications = models.ManyToManyField(Application)
