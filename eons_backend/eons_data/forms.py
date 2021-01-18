from django.forms import ModelForm

from .models import EonsCsv


class EonsCsvForm(ModelForm):
    class Meta:
        model = EonsCsv
        fields = ['site_code', 'file_name']