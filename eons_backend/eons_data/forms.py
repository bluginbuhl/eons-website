from django.forms import ModelForm, ClearableFileInput

from .models import EonsCsv


class EonsCsvForm(ModelForm):
    class Meta:
        model = EonsCsv
        fields = [
            'station_code',
            'file_name',
            ]