from .models import Location
from rest_framework import serializers


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ['name', 'lon', 'lat', 'location_type', 'location_description']
