from django import forms
from django.forms import HiddenInput
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
            Add placeholders and classes, set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'user_name': 'User Name',
            'email': 'Email Address',
            'author_name': 'Author Name',
            'image_url': 'Image url',
            'note': 'Note'
        }

        self.fields['is_approved'].widget = HiddenInput()

        gallerycategories = GalleryCategory.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in gallerycategories]

        self.fields['gallery_category'].choices = friendly_names

        self.fields['user_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field == 'user_name' or field == 'email' or field == 'author_name' or field == 'image_url' or field == 'note':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-grey rounded-10'


class AdminGalleryForm(forms.ModelForm):

    class Meta:
        model = Gallery
        fields = '__all__'

    image = forms.ImageField(required=True, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        """
            Add placeholders and classes, set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'user_name': 'User Name',
            'email': 'Email Address',
            'author_name': 'Author Name',
            'image_url': 'Image url',
            'note': 'Note'
        }

        gallerycategories = GalleryCategory.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in gallerycategories]

        self.fields['gallery_category'].choices = friendly_names

        self.fields['user_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field == 'user_name' or field == 'email' or field == 'author_name' or field == 'image_url' or field == 'note':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-grey rounded-10'
