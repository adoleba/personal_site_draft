from django import forms
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, initial=' ',
                           error_messages={'required': _("Please fill your name")},
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=50, initial=' ',
                             error_messages={
                                 'required': _("Please fill your email address"),
                                 'invalid': _("The email address is not valid")
                             },
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(max_length=50, initial=' ',
                              error_messages={'required': _("Please fill the subject of the message")},
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}),
                           initial=' ', error_messages={'required': _("Please fill the content of message")})

    def clean(self):
        cleaned_data = super().clean()

        for field in cleaned_data:
            field_value = cleaned_data.get(field)
            if field_value == ' ':
                self.add_error(field_value, '')
