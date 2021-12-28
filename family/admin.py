from django.contrib import admin
from .models import Family, FamilyCalendar


class FamilyAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'first_name', 'last_name', 'email', 'sity', 'created',
    ]
    search_fields = ('first_name', 'last_name', 'email', 'sity', 'created')


admin.site.register(Family, FamilyAdmin)
admin.site.register(FamilyCalendar)
