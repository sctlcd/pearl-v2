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
    image = models.ImageField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    # date = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return f'{self.user_name} on gallery category {self.gallery_category}'

# Products models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254, null=True, blank=False)
    friendly_name = models.CharField(max_length=254, null=True, blank=False)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=False, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2,  default=0, null=True, blank=False)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True, default=0)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
