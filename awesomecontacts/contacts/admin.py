from contacts.models import Contact
from django.contrib import admin

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'phone_number',
                    'job', 'company', 'email')
