from django.db import models


# Contact models

class Contact(models.Model):
    first_name = models.CharField(max_length=254, null=False, blank=False)
    last_name = models.CharField(max_length=254, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} \'s request on {self.date}'
