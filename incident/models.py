from django.db import models
from user.models import User

# Create your models here.

class Incident(models.Model):
    users = models.ManyToManyField(User,related_name='incidents')
    incident_id = models.CharField(primary_key=True, max_length=12, unique=True,blank=True,editable=False)
    incident_name = models.CharField(max_length=100)
    Reporter_name = models.CharField(max_length=100)
    incident_details = models.TextField()
    reported_at = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=100) #High, Medium, Low
    status = models.CharField(max_length=100, default="Open") #open, in process, closed
    
    def __str__(self):
        return self.incident_name
     