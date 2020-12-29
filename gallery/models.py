from django.db import models


# Gallery models

class GalleryCategory(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254, null=True, blank=False)
    friendly_name = models.CharField(max_length=254, null=True, blank=False)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Gallery(models.Model):

    class Meta:
        verbose_name_plural = 'Gallery'

    user_name = models.CharField(max_length=254, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    author_name = models.CharField(max_length=254, null=False, blank=False)
    gallery_category = models.ForeignKey('GalleryCategory', null=True, blank=False, on_delete=models.SET_NULL)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(upload_to='gallery', null=False, blank=False)
    note = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    is_approved = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return f'{self.user_name}\'s image in {self.gallery_category} gallery category'
