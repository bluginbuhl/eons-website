from rest_framework import serializers

from .models import EonsSite


class EonsSiteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('site_code', 'name', 'date_added', 'latitude', 'longitude')
        model = EonsSite