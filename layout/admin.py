from django.contrib import admin
from . models import Newsletter, ContactMessage


class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_added')


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'contact_message', 'date_added')


admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
