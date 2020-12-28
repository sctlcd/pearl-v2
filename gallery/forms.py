from django import forms
from django.forms import ModelForm, HiddenInput
from .widgets import CustomClearableFileInput
from .models import Gallery, GalleryCategory


# Gallery forms

class GalleryForm(forms.ModelForm):

    class Meta:
        model = Gallery
        fields = '__all__'

    image = forms.ImageField(required=True, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        """
            Set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        self.fields['is_approved'].widget = HiddenInput()

        gallerycategories = GalleryCategory.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in gallerycategories]

        self.fields['gallery_category'].choices = friendly_names

        self.fields['user_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'border-grey text-grey rounded-10'


class AdminGalleryForm(forms.ModelForm):

    class Meta:
        model = Gallery
        fields = '__all__'

    image = forms.ImageField(required=True, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        """
            Set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        gallerycategories = GalleryCategory.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in gallerycategories]

        self.fields['gallery_category'].choices = friendly_names

        self.fields['user_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'border-grey text-grey rounded-10 profile-form-input'
