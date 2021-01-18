from rest_framework import serializers

from .models import EonsSite, EonsCsv


class EonsSiteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('site_code', 'name', 'date_added', 'latitude', 'longitude')
        model = EonsSite


class EonsCsvSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('site_code', 'file_name', 'uploaded_date', 'user')
        model = EonsCsv