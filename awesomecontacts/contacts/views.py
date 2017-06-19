from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from contacts.forms import ContactForm
from django.views import View
from contacts.models import Contact

# Create your views here.

class MainView(View):

    def get(self, request):
        contacts = Contact.objects.all().order_by('last_name')
        return render(request, 'contacts/main_page.html', {'contacts': contacts})


def delete_contact(request, pk):
    obj = get_object_or_404(Contact, pk=pk)
    obj.delete()
    return HttpResponse("Congrats, you deleted a contact")



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
            return redirect('contact-detail')


class ContactDetail(View):

    def get(self, request):
        contact = Contact.objects.last()
        return render(request, 'contacts/contact-detail.html', {'contact': contact})



