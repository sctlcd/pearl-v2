from django.shortcuts import render


# Gallery views

def gallery(request):
    """
        A view to return the gallery page
    """
    return render(request, 'gallery/gallery.html')


def gallery_share(request):
    """
        A view to return the gallery form to share your own work of art
    """
    return render(request, 'gallery/gallery_share.html')
