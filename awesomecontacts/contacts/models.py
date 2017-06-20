from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Contact(models.Model):
    last_name = models.CharField(max_length=64, null=False)
    name = models.CharField(max_length=64, null=False)
    phone_number = PhoneNumberField()
    job = models.CharField(max_length=64, null=False)
    company = models.CharField(max_length=64, null=False)
    email = models.EmailField(null=False)

    def __str__(self):
        return '%s %s %s %s %s %s' % (self.last_name, self.name,
                                self.phone_number, self.job,
                                self.company, self.email)
