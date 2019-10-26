from .models import Locations
from rest_framework import serializers


class LocationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Locations
        fields = ['name', 'lon', 'lat', 'location_type', 'location_description']
