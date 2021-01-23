from rest_framework import serializers

from .models import EonsStation, EonsCsv


class EonsStationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('station_code', 'name', 'date_added', 'latitude', 'longitude')
        model = EonsStation


class EonsCsvSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'station_code',
            'file_name',
            'uploaded_date',
            'user',
            )
        model = EonsCsv