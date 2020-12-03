from django.shortcuts import render


# Gallery views

def gallery(request):
    """ A view to return the gellery page
    """
    return render(request, 'gallery/gallery.html')
