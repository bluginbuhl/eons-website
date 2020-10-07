from django.contrib import admin
from guardian.admin import GuardedModelAdmin

from .models import EonsSite


class EonsSiteAdmin(GuardedModelAdmin):
    list_display = ('site_code', 'name', 'users_list')

admin.site.register(EonsSite, EonsSiteAdmin)