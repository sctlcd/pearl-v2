from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Gallery, GalleryCategory
from .forms import GalleryForm


# Gallery views

def gallery(request):
    """
        A view to return the gallery page
    """

    template = 'gallery/gallery.html'
    context = {
        'gallery': gallery,
        'current_categories': gallery_categories,
    }

    return render(request, template, context)


def gallery_share(request):
    """
        A view to return the gallery form to share your own work of art
    """
    if request.method == 'POST':
        gallery_form = GalleryForm(request.POST, request.FILES)
        if gallery_form.is_valid():
            gallery_form.save()
            messages.success(request, 'Succeed to send your request for sharing your work of art!')
            return redirect(reverse('gallery_share'))
        else:
            messages.error(request, 'Failed to send your request for sharing your work of art. Please ensure the gallery form is valid.')
    else:
        gallery_form = GalleryForm()

    template = 'gallery/gallery_share.html'
    context = {
        'gallery_form': gallery_form,
    }

    return render(request, template, context)
