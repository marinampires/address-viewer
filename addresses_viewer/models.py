from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .fusion_tables import save

class Address(models.Model):
    lat = models.DecimalField(max_digits=10, decimal_places=6)
    lng = models.DecimalField(max_digits=10, decimal_places=6)
    address_name = models.CharField(max_length=500)

    class Meta:
        unique_together = (("lat", "lng"),)

@receiver(post_save, sender=Address)
def save_fusion_table(sender, instance, **kwargs):    
    save(instance)