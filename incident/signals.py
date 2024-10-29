from django.db.models.signals import pre_save
from django.dispatch import receiver
from datetime import datetime
import uuid
from .models import Incident


@receiver(pre_save, sender=Incident)
def generate_incident_id(sender, instance, **kwargs):
    if not instance.incident_id:   
        
        random_number = str(uuid.uuid4().int)[:5]
        current_year = str(datetime.now().year)
        id_format = f"RMS{random_number}{current_year}"
        instance.incident_id = id_format