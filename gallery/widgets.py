from django.forms.widgets import FileInput


class CustomFileInput(FileInput):
    template_name = 'gallery/custom_widget_templates/custom_file_input.html'
