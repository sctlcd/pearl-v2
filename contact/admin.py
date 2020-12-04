from django.contrib import admin
from .models import Contact


# Contact admin

class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'email',
        'subject',
        'message',
    )

    ordering = ('last_name', 'first_name')


admin.site.register(Contact, ContactAdmin)
