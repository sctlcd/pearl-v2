from django import forms

from .models import Contact


# Contact form

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'message')


def __init__(self, *args, **kwargs):
    """
        Set autofocus on first field
    """
    super().__init__(*args, **kwargs)

    self.fields['first_name'].widget.attrs['autofocus'] = True

    for field_name, field in self.fields.items():
        field.widget.attrs['class'] = 'border-grey rounded'
