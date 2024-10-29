"""
URL configuration for incidentMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.contrib.auth.mixins import LoginRequiredMixin

from .views import Home_Page, Registration_page,location_view
from user.views import logout
urlpatterns = [
    #/admin and linking Pages
    path("admin/", admin.site.urls),
    path('user/', include('user.urls')),
    path('incident/', include('incident.urls')),

    # /Static Pages
    path('', Home_Page, name='home'),
    path('register/',Registration_page , name='register'),

    #----------reset password -------------
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='reset_password/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='reset_password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="reset_password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='reset_password/password_reset_complete.html'), name='password_reset_complete'),

    #API for Location 
    path('get-location/', location_view, name='get_location'),

    #Login and Logout
    path('login/',auth_views.LoginView.as_view(template_name='frontend/login_page.html') , name='login'),
    path('logout/',logout, name='logout'),

]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
