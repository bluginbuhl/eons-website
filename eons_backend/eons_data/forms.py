from django.forms import ModelForm

from .models import EonsCsv


class EonsCsvForm(ModelForm):
    class Meta:
        model = EonsCsv
        fields = [
            'station_code',
            'file_name',
            ]