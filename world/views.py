from django.shortcuts import render

# Create your views here.
from .models import Locations
from rest_framework import viewsets
from .serializers import LocationsSerializer


class LocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Locations.objects.all()
    serializer_class = LocationsSerializer