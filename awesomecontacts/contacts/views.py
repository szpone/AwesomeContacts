from django.shortcuts import render, HttpResponse
# from django.views.generic.edit import FormView
from contacts.forms import ContactForm
from django.views import View

# Create your views here.

def index(request):
    return HttpResponse("Elo")

class ContactFormView(View):

    def get(self, request):
        form = ContactForm()
        return render(request, 'contact.html',
                    {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            job = form.cleaned_data['job']
            company = form.cleaned_data['company']
            email = form.cleaned_data['email']
            return HttpResponse("Thx!")


