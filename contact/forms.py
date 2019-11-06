from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="Imię i nazwisko", max_length=50, initial=' ',
                           error_messages={'required': "Uzupełnij dane nadawcy"},
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Adres email", max_length=50, initial=' ',
                             error_messages={
                                 'required': "Uzupełnij adres email",
                                 'invalid': "Podany adres e-mail nie jest poprawny"
                             },
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(label="Temat wiadomości", max_length=50, initial=' ',
                              error_messages={'required': "Uzupełnij temat wiadomości"},
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}),
                           initial=' ', error_messages={'required': "Uzupełnij treść wiadomości"})

    def clean(self):
        cleaned_data = super().clean()

        for field in cleaned_data:
            field_value = cleaned_data.get(field)
            if field_value == ' ':
                self.add_error(field_value, '')
