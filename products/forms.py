from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


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

        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        # friendly_names[:0] = [('', 'Select a category')]
        self.fields['category'].choices = friendly_names

        self.fields['category'].widget.attrs['autofocus'] = True

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'
