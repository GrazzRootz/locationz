from django.shortcuts import render

# Create your views here.
from .models import Location
from rest_framework import viewsets
from .serializers import LocationSerializer


class LocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer