from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import EonsUserCreationForm, EonsUserChangeForm
from .models import EonsUser


class EonsUserAdmin(UserAdmin):
    add_form = EonsUserCreationForm
    form = EonsUserChangeForm
    model = EonsUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active',)
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(EonsUser, EonsUserAdmin)

admin.site.site_title = "EONS - Admin"
admin.site.site_header = "EONS Administration"