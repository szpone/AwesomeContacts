from django.db import models

# Create your models here.

class Contacts(models.Model):
    name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=64, null=False)
    phone_number = models.IntegerField()
    job = models.CharField(max_length=64, null=False)
    company = models.CharField(max_length=64, null=False)
    email = models.EmailField(null=False)
