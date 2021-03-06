"""awesomecontacts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from contacts.views import ContactFormView, ContactDetail, MainView, delete_contact, update_contact
from django.conf.urls import url
from django.contrib import admin

admin.site.site_header = 'AwesomeContacts Administration'
admin.site.site_title = 'AwesomeContacts Administration'

urlpatterns = [
    # I changed default admin URL for safety reasons
    url(r'^awscontact/', admin.site.urls),
    url(r'^$', MainView.as_view(), name='main-page'),
    url(r'^add-contact/', ContactFormView.as_view(), name='add-contact'),
    url(r'^contact-detail/', ContactDetail.as_view(), name='contact-detail'),
    url(r'^delete-contact/(?P<pk>\d+)/?$', delete_contact, name='delete-contact'),
    url(r'^update-contact/(?P<pk>\d+)/$', update_contact, name='update-contact'),

]
