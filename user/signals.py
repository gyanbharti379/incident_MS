from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from .models import LoginAttempts

from django.dispatch import receiver
from .models import User
from django.utils import timezone

@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    login_attempt = LoginAttempts.objects.get(user=user)
    LoginAttempts.increment_success_login_count(login_attempt)

    print("login success")
    print("user Name: ",user.get_full_name()) 
    print("user logged in at: ", user.last_login)

   
@receiver(user_logged_out, sender=User)
def logout_success(sender, request, user, **kwargs):
    print("logout success")
    print("user Name: ",user.get_full_name()) 
    print("user logged out at: ", timezone.now())

@receiver(user_login_failed)
def login_failed(sender, credentials, request, **kwargs):
    try:
     
        email = request.POST.get('email')
        user = User.objects.get(email=email)
        if user is not None:
            print("User with provided email exists.")    
            login_attempt = LoginAttempts.objects.get(user=user)
            LoginAttempts.increment_failed_login_count(login_attempt)
            print("Login failed due to wrong password")
 
    except User.DoesNotExist:
        print("---------login failed----------")
        print("User with provided email does not exist.")    
        print("user Email: ",request.POST.get('email'))
        print("password: ",request.POST.get('password')) 
        print("user trying to login at: ", timezone.now())
    

@receiver(user_logged_in)
def create_login_attempts(sender, request, user, **kwargs):
    login_attempt, created = LoginAttempts.objects.get_or_create(user=user)
    login_attempt.save()
    


 
