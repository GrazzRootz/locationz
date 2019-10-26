from django.db import models


class Locations(models.Model):
    name = models.CharField(max_length=128)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    location_type = models.CharField(max_length=128)
    location_description = models.CharField(max_length=18)