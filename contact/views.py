from django.shortcuts import redirect
from django.views.generic import FormView

from contact.forms import ContactForm


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact/contact.html'
