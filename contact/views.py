from django.shortcuts import render

from .forms import ContactForm

# Contact views


def contact(request):
    template = 'contact/contact.html'

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            contact_form.save()

    else:
        contact_form = ContactForm()

    context = {
        'contact_form': contact_form,
    }
    return render(request, template, context)
