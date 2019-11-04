from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, DetailView
from django.views.generic.base import View

from contact.forms import ContactForm


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact/contact.html'
    success_url = reverse_lazy('contact:thank_you')


class ThankYouView(View):

    def get(self, request):
        return render(request, 'contact/thank_you.html')
