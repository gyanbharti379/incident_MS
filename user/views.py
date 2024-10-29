from datetime import datetime, timezone


from incident.models import Incident
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import get_user_model,update_session_auth_hash
from django.contrib.auth import authenticate,login,logout as auth_logout
from user.forms import UserForm, UserRegisterForm

 

from .models import Category, User

User = get_user_model()

# Create your views here.
#After submitting registration form land here-------->


def submitUserRegistrationForm(request):
    try:
        last_login = datetime.now(timezone.utc)
        if request.method == "POST":
            f_name = request.POST.get('fname')
            l_name = request.POST.get('lname')
            email = request.POST.get('email')
            password = request.POST.get('password1')
            address = request.POST.get('address')
            country = request.POST.get('country')
            state = request.POST.get('state')
            city = request.POST.get('city')
            pincode = request.POST.get('pincode')
            std = request.POST.get('std')
            mobile_no = request.POST.get('mobile_no')
            fax = request.POST.get('fax')
            phone = request.POST.get('phone')
            cat = request.POST.get('category')

            user = User.objects.create_user(
                username=f_name+l_name, 
                email=email, 
                password=password,
                first_name = f_name,
                last_name = l_name,
                last_login = last_login,
                std = std,
                mobile_no = mobile_no,
                fax = fax,
                phone_no = phone,
                address = address,
                country = country,
                state = state,
                city = city,
                pincode = pincode,
              
                date_joined = last_login,
                image = 'media/images/user.png',
                category = Category.objects.create(
                    name = cat,
                    description = "description"
                    )

                )
            user.save()
         
            return render(request, "frontend/registration_page.html",{
                'result':"Data Saved Successfully"
            })
                             
        else:
            return render(request, "frontend/registration_page.html",{
            'result':"Data Not Saved fill details correctly"
            })
    except Exception as e:
            print(e) 
    return render(request, "frontend/registration_page.html"  )

#------------Login Functionality -------------

def submitLoginForm(request):

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = authenticate(request, username=email,password=password)
        
            if user is not None:
                login(request,user)
                user_id = user.id
                name = user.get_full_name()
                cat = Category.objects.get(id=user.category_id)
                incs = user.incidents.all()
 
                #---store important data from session ---->
                request.session["user_id"] = user_id
                request.session["Name"] = name
                request.session["Cat_name"] = cat.name
              
                #---retrieve useful data from session ---->
                name = request.session.get("Name")
                cat = request.session.get("Cat_name")

                return render(request, 'backend/userDashboard.html',{
                    'name':name,
                    'cat':cat,
                    'incidents':incs,
                })
                    
            else:
            
                return render(request, "frontend/login_page.html",{
                'result':"Login Failed"
            })
                 
              
        except User.DoesNotExist:
                return render(request, "frontend/login_page.html",{
                'result':"User Not Found"
            })
                            
        except User.MultipleObjectsReturned:
                    
               return render(request, "frontend/login_page.html",{
                'result':"Multiple User found, please contact support."})
                            
        except Exception as e:
                print(e)
                return render(request, "frontend/login_page.html",{
                'result':e,
            }) 
 

#-After Login land here --------------->
@login_required(login_url='login')
def UserDashBoard_page(request):
    user_id = request.session.get("user_id")
    user = User.objects.get(id=user_id)
    incs = user.incidents.all()

    #---retrieve useful data from session ---->
    name = request.session.get("Name")
    cat = request.session.get("Cat_name")

    return render(request, 'backend/userDashboard.html',
        {
            'name':name,
            'cat':cat,
            'incidents':incs, 
        })
        

@login_required(login_url='login')
def updateProfile(request):
    user_id = request.session.get("user_id")
    name = request.session.get("Name")
    cat = request.session.get("Cat_name")
    return render(request, 'backend/updateProfile.html',{
        'user_id':user_id,
        'name':name,
        'cat':cat})

@login_required(login_url='login')
def changePasswordForm(request):

    form = PasswordChangeForm(user = request.user)

    user_id = request.session.get("user_id")
    name = request.session.get("Name")
    cat = request.session.get("Cat_name")
    return render(request, 'backend/change_password_form.html',{
        'user_id':user_id,
        'name':name,
        'cat':cat,
        'form':form,
        'result':"",
        })


@login_required(login_url='login')
def changePassword(request):

    if request.method == "POST":
       
        form = PasswordChangeForm(user = request.user, data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
          
    user_id = request.session.get("user_id")
    name = request.session.get("Name")
    cat = request.session.get("Cat_name")

    return render(request, 'backend/change_password_form.html',{
        'user_id':user_id,
        'name':name,
        'cat':cat,
        'result':"Password Changed Successfully",})

@login_required(login_url='login')
def viewProfile(request):
    user_id = request.session.get("user_id")
    user = User.objects.get(id=user_id)

    name = request.session.get("Name")
    cat = request.session.get("Cat_name")

    return render(request, 'backend/userDetails.html',{
        'f_name':user.first_name,
        'l_name':user.last_name,
        'email':user.email,
        'phone':user.phone_no,
        'std':user.std,
        'fax':user.fax,
        'mobile':user.mobile_no,
        'address':user.address,
        'city':user.city,
        'state':user.state,
        'pincode':user.pincode,
        'country':user.country,
        'cat_name':user.category.name,
        'name':name,
        'cat':cat,})


@login_required(login_url='login')
def logout(request):
    auth_logout(request)
    return render(request, 'frontend/logout_page.html')

 