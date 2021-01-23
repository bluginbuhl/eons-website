from django.contrib import admin
from guardian.admin import GuardedModelAdmin
from django import forms

from .models import EonsStation, EonsSensor, EonsCsv, EonsBaseData


class EonsSensorInline(admin.TabularInline):
    model = EonsSensor
    max_num = 2

@admin.register(EonsStation)
class EonsStationAdmin(GuardedModelAdmin):
    inlines = [
        EonsSensorInline
    ]
    list_display = ('station_code', 'name', 'sensors', 'users')

    def sensors(self, obj):
        return obj.sensors_list()

    def users(self, obj):
        return obj.users_list()

@admin.register(EonsSensor)
class EonsSensorAdmin(GuardedModelAdmin):
    list_display = ('sensor_id', 'station_code', 'is_snow_sensor')

@admin.register(EonsCsv)
class EonsCsvAdmin(GuardedModelAdmin):
    list_display = (
        'id', 
        'converted_to_raw_data',
        'get_filestring',
        'station_code',
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
    station = forms.CharField(widget=forms.TextInput(attrs={'size': 400}))

@admin.register(EonsBaseData)
class EonsBaseDataAdmin(GuardedModelAdmin):
    list_display = (
        'station',
        'utc_datetime',
    )
