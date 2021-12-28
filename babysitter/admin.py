from django.contrib import admin
from .models import Babysitter, BabysitterCalendar


class BabysitterAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'first_name', 'last_name', 'email', 'sity', 'created', 'sex', 'age',
    ]
    search_fields = ('first_name', 'last_name', 'email', 'sity', 'created')


admin.site.register(Babysitter, BabysitterAdmin)
admin.site.register(BabysitterCalendar)
