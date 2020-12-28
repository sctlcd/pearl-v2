from django import forms
from .models import Contact


# Contact form

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'


def __init__(self, *args, **kwargs):
    """
        Set autofocus on first field
    """
    super().__init__(*args, **kwargs)

    self.fields['first_name'].widget.attrs['autofocus'] = True

    for field in self.fields:
        self.fields[field].widget.attrs['class'] = 'border-grey text-grey rounded-10'

    # for field_name, field in self.fields.items():
    #     field.widget.attrs['class'] = 'border-grey text-grey rounded-10'
