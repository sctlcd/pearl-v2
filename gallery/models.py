from django.db import models


# Gallery models

class GalleryCategory(models.Model):

    class Meta:
        verbose_name_plural = 'Gallery categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Gallery(models.Model):
    user_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    author_name = models.CharField(max_length=50, null=False, blank=False)
    gallery_category = models.ForeignKey('GalleryCategory', null=True, blank=True, on_delete=models.SET_NULL)
    image_url = models.URLField(max_length=1024, null=False, blank=False)
    image = models.ImageField(null=False, blank=False)
    note = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
