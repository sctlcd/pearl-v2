from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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


@login_required
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
        'on_share_gallery_page': True
    }

    return render(request, template, context)


@login_required
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
        admin_gallery_form = AdminGalleryForm()

    template = 'gallery/add_gallery.html'
    context = {
        'admin_gallery_form': admin_gallery_form,
    }

    return render(request, template, context)


@login_required
def edit_gallery(request, gallery_id):
    """
        Edit a galery image to the gallery
    """
    gallery_item = get_object_or_404(Gallery, pk=gallery_id)
    if request.method == 'POST':
        admin_gallery_form = AdminGalleryForm(request.POST, request.FILES, instance=gallery_item)
        if admin_gallery_form.is_valid():
            gallery_item = admin_gallery_form.save()
            messages.success(request, 'Succeed to edit gallery image!')
            return redirect(reverse('gallery'))
        else:
            messages.error(request, 'Failed to update gallery image. Please ensure the gallery form is valid.')
    else:
        admin_gallery_form = AdminGalleryForm(instance=gallery_item)
        messages.info(request, f'You are editing {gallery_item.user_name}\'s image')

    template = 'gallery/edit_gallery.html'
    context = {
        'admin_gallery_form': admin_gallery_form,
        'gallery_item': gallery_item,
    }

    return render(request, template, context)


@login_required
def delete_gallery(request, gallery_id):
    """
        Delete a gallery image from the gallery
    """
    gallery_item = get_object_or_404(Gallery, pk=gallery_id)
    gallery_item.delete()
    messages.success(request, 'Gallery image deleted!')
    return redirect(reverse('gallery'))
