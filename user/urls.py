from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (UserDashBoard_page, submitLoginForm,
    changePasswordForm,submitUserRegistrationForm, updateProfile, viewProfile, changePassword)

urlpatterns = [
    path('submitUserRegistrationForm/',submitUserRegistrationForm, name='submitUserRegistrationForm'),
    path('submitLoginForm/',submitLoginForm, name='submitLoginForm'),
    path('userdashboard/',UserDashBoard_page, name='userdashboard'),
    path('updateProfile/',updateProfile, name='updateProfile'),
    path('viewProfile/',viewProfile, name='viewProfile'),
    path('changePasswordForm/',changePasswordForm, name='changePasswordForm'),
    path('submitPasswordChangeForm/',changePassword, name='submitPasswordChangeForm'),

]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
