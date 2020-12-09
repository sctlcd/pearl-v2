from django import forms

from .models import Contact


# Contact form

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'message')


def __init__(self, *args, **kwargs):
    """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
    """
    super().__init__(*args, **kwargs)
    # placeholders = {
    #     'first_name': 'First name',
    #     'last_name': 'Last name',
    #     'email': 'Email',
    #     'message': 'Message',
    # }
    #
    # self.fields['first_name'].widget.attrs['autofocus'] = True
    # for field in self.fields:
    #     if self.fields[field].required:
    #         placeholder = f'{placeholders[field]} *'
    #     else:
    #         placeholder = placeholders[field]
    #     self.fields[field].widget.attrs['placeholder'] = placeholder
    #     self.fields[field].widget.attrs['class'] = 'contact-style-input'
    #     self.fields[field].label = False
