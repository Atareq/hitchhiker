from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Shipment
@receiver(post_save, sender=Shipment)
def update_quantity(sender, instance, created, **kwargs):
    if created:       
        instance.quantity += 1
        instance.save()
