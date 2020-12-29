from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


# Product form

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label="Image", required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        """
            Add placeholders and classes, set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'sku': 'Sku',
            'name': 'Name',
            'description': 'Description',
            'image_url': 'Image url',
        }

        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names

        self.fields['category'].widget.attrs['autofocus'] = True

        # for field_name, field in self.fields.items():
        for field in self.fields:
            if field == 'sku' or field == 'name' or field == 'description' or field == 'image_url':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            # field.widget.attrs['class'] = 'border-grey rounded-10'
            self.fields[field].widget.attrs['class'] = 'border-grey rounded-10'
