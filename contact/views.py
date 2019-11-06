from django.contrib import messages
from django.core.mail import EmailMessage
from django.http import request
from django.shortcuts import render
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import FormView, DetailView
from django.views.generic.base import View

from contact.forms import ContactForm
from personal_site import settings


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact/contact.html'
    success_url = reverse_lazy('contact:thank_you')

    def form_valid(self, form):
        self.send_mail(form.cleaned_data)
        return super().form_valid(form)

    def form_invalid(self, form):
        for field in form.errors:
            error_message_html = form.errors[field].as_data()
            error_message = str(error_message_html[0]).strip("[]'")
            form[field].field.widget.attrs['class'] += ' input-error'
            messages.error(self.request, error_message)
        return super().form_invalid(form)

    def send_mail(self, valid_data):
        template = get_template('contact/email.html')
        content = template.render(valid_data)

        email = EmailMessage(
            "Wiadomość z formularza kontaktowego",
            content,
            str(valid_data['name']),
            [settings.EMAIL_HOST_USER],
            headers={'Reply-To': valid_data['email']}
        )
        email.content_subtype = 'html'
        email.send()


class ThankYouView(View):

    def get(self, request):
        return render(request, 'contact/thank_you.html')
