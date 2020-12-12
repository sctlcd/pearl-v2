from django import forms

from .models import Gallery


# Contact form

class ContactForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = '__all__'
