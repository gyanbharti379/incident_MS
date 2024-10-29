from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from .views import IncidentViewSet
from .views import Create_Incident_page, Edit_Incident_page, User_Details_page,submitIncidentForm,updateIncidentForm,Search_Incident_page

router = routers.DefaultRouter()
router.register(r'incident', IncidentViewSet, basename='incident')

urlpatterns = [
     
    #Static Pages
    path('createIncident/',Create_Incident_page, name='createIncident'),
    path('viewIncident/<email>/',User_Details_page, name='viewIncident'),
    path('editIncident/<incident_id>/',Edit_Incident_page, name='editIncident'),
    path('searchIncident/',Search_Incident_page, name='searchIncident'),
   
    #Dynamic Pages
    path('submitIncidentForm',submitIncidentForm, name='submitIncidentForm'),
    path('updateIncidentForm',updateIncidentForm, name='updateIncidentForm'),

    #API Pages
    path('api/', include(router.urls)),
 
  
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
