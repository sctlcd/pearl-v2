from django import forms

from .models import Gallery


# Contact form

class ContactForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = '__all__'


def __init__(self, *args, **kwargs):
    """
        
    """
    super().__init__(*args, **kwargs)
