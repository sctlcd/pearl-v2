from django.contrib import admin
from .models import Gallery, GalleryCategory


# Gallery admin

class GalleryAdmin(admin.ModelAdmin):
    list_display = (
        'uploaded_at',
        'user_name',
        'email',
        'author_name',
        'gallery_category',
        'image',
        'is_approved',
    )
    
    ordering = ('uploaded_at',)


class GalleryCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(GalleryCategory, GalleryCategoryAdmin)
