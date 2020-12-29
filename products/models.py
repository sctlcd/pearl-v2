from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


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
    price = models.DecimalField(max_digits=6, decimal_places=2,  default=0, null=False, blank=False)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True, default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
