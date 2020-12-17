from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Gallery, GalleryCategory
from .forms import GalleryForm, AdminGalleryForm


# Gallery views

def gallery(request):
    """
        A view to return the gallery page
    """

    gallery = Gallery.objects.all()
    gallery_categories = GalleryCategory.objects.all()

    template = 'gallery/gallery.html'
    context = {
        'gallery': gallery,
        'current_categories': gallery_categories,
    }

    return render(request, template, context)


def share_gallery(request):
    """
        A view to return the gallery form to share your own work of art
    """
    if request.method == 'POST':
        gallery_form = GalleryForm(request.POST, request.FILES)
        if gallery_form.is_valid():
            gallery_form.save()
            messages.success(request, 'Your request for sharing your work of art has been sent successfully!')
            return redirect(reverse('share_gallery'))
        else:
            messages.error(request, 'Your request for sharing your work of art has failed. Please ensure the gallery form is valid.')
    else:
        gallery_form = GalleryForm()

    template = 'gallery/share_gallery.html'
    context = {
        'gallery_form': gallery_form,
    }

    return render(request, template, context)


def add_gallery(request):
    """
        Add a galery image to the gallery
    """
    if request.method == 'POST':
        admin_gallery_form = AdminGalleryForm(request.POST, request.FILES)
        if admin_gallery_form.is_valid():
            admin_gallery_form.save()
            messages.success(request, 'Succeed to add a gallery image!')
            return redirect(reverse('gallery'))
        else:
            messages.error(request, 'Failed to add a gallery image. Please ensure the gallery form is valid.')
    else:
        admin_gallery_form = GalleryForm()

    template = 'gallery/add_gallery.html'
    context = {
        'admin_gallery_form': admin_gallery_form,
    }

    return render(request, template, context)
