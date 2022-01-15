from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model


class CustomUserAdmin(UserAdmin):
    """Define admin model for custom User model with no username field."""
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                      'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'user_type', 'is_email_verified',
                    'is_terms_confirmed', 'membership', 'is_staff', 'date_joined')
    search_fields = ('email', 'user_type', 'is_email_verified',
                     'is_terms_confirmed', 'membership', 'date_joined')
    ordering = ('date_joined',)


admin.site.register(get_user_model(), CustomUserAdmin)
