from django.shortcuts import render, HttpResponse, redirect
# from django.views.generic.edit import FormView
from contacts.forms import ContactForm
from django.views import View
from contacts.models import Contact

# Create your views here.

def index(request):
    return HttpResponse("Elo")


class ContactFormView(View):

    def get(self, request):
        form = ContactForm()
        return render(request, 'contacts/contact.html',
                    {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            obj = Contact()
            obj.name = form.cleaned_data['name']
            obj.last_name = form.cleaned_data['last_name']
            obj.phone_number = form.cleaned_data['phone_number']
            obj.job = form.cleaned_data['job']
            obj.company = form.cleaned_data['company']
            obj.email = form.cleaned_data['email']
            obj.save()
            return redirect('contacts/contact-detail')


class ContactDetail(View):

    def get(self, request):
        contact = Contact.objects.last()
        return render(request, 'contacts/contact-detail.html', {'contact': contact})



