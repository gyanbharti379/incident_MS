from django.contrib import admin
from .models import Incident

# Register your models here.

admin.site.site_header = "Incident Management System"
admin.site.register(Incident)