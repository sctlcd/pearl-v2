from django.contrib import admin
from .models import Contact


# Contact admin

class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'date',
        'first_name',
        'last_name',
        'email',
        'message',
    )

    ordering = ('date',)


admin.site.register(Contact, ContactAdmin)
