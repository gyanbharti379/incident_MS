from rest_framework import serializers
from .models import Incident
from django.contrib.auth.models import User

class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = 'incident_id', 'incident_name', 'Reporter_name', 'incident_details', 'reported_at', 'priority', 'status'