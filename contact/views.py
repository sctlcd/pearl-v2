from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import ContactForm


# Contact views

def contact(request):
    '''
        A view to return the contact page
    '''

    if request.method == 'POST':
        contact_form = ContactForm(request.POST, request.FILES)

        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Your contact request has been sent successfully!')
            return redirect(reverse('contact'))
        else:
            messages.error(request, 'Your contact request has failed. Please ensure the contact form is valid.')
    else:
        contact_form = ContactForm()

    template = 'contact/contact.html'

    context = {
        'contact_form': contact_form,
        'on_contact_page': True
    }

    return render(request, template, context)
