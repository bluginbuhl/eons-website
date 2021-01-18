from django.contrib import admin
from guardian.admin import GuardedModelAdmin
from django import forms

from .models import EonsSite, EonsCsv, EonsBaseData


class EonsSiteAdmin(GuardedModelAdmin):
    list_display = ('site_code', 'name', 'users_list')

class EonsCsvAdmin(GuardedModelAdmin):
    list_display = (
        'id', 
        'activated',
        'get_filestring',
        'site_code',
        'uploaded_date',
        'user'
        )

    list_display_links = (
        'get_filestring',
    )

    def render_change_form(self, request, context, *args, **kwargs):
        self.change_form_template = 'admin/eons_data/change_form_help_text.html'
        extra = {
            'help_text': "EONS CSV files are uploaded to /media/unprocessed/ before they are processed. Once they are uploaded, the 'activated' flag will be automatically set unless there is a problem.",
        }

        context.update(extra)

        return super(EonsCsvAdmin, self).render_change_form(request, context, *args, **kwargs)

    def get_filestring(self, obj):
        return str(obj.file_name.name).split('/')[-1]
    get_filestring.short_description = "file name"

class EonsBaseDataAdminForm(forms.ModelForm):
    site_code = forms.CharField(widget=forms.TextInput(attrs={'size': 400}))

class EonsBaseDataAdmin(GuardedModelAdmin):
    list_display = (
        'site_code',
        'utc_datetime'
    )


admin.site.register(EonsSite, EonsSiteAdmin)
admin.site.register(EonsCsv, EonsCsvAdmin)
admin.site.register(EonsBaseData, EonsBaseDataAdmin)