from django.db import models

class Address(models.Model):
    lat = models.DecimalField(max_digits=10, decimal_places=6)
    lng = models.DecimalField(max_digits=10, decimal_places=6)
    address_name = models.CharField(max_length=500)
    place_id = models.CharField(max_length=50, unique=True)

