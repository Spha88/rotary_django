from django.contrib import admin
from .models import ContactMessage

class ContactMessageAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'email', 'subject', 'message', )

admin.site.register(ContactMessage, ContactMessageAdmin)
