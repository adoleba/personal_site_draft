from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="Imię i nazwisko", max_length=50,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Adres email", max_length=50,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(label="Temat wiadomości", max_length=50,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
