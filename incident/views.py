from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from datetime import datetime, timezone
from .models import Incident
from django.contrib import messages
from user.models import User, Category
from rest_framework import viewsets
from .serializers import IncidentSerializer
# Create your views here.


#-------------------------AREA for API---- Begin ------
class IncidentViewSet(viewsets.ModelViewSet):
    queryset = Incident.objects.all()   
    serializer_class = IncidentSerializer

#-------------------------AREA for API---- End ------

# --This area for handling incidents ( create, view and edit) ------------------>

# --------------Handle Static Pages ------------------>
@login_required(login_url='login')
def Create_Incident_page(request):
    user_id = request.session.get("user_id")
    name = request.session.get("Name")
    cat = request.session.get("Cat_name")
    return render(request, 'backend/create_incident.html',{
        'user_id':user_id,
        'name':name,
        'cat':cat})

@login_required(login_url='login')
def Search_Incident_page(request):
    try:
        if request.method == "POST":
            inc_id = request.POST.get('search')
            incident = get_object_or_404(Incident, incident_id=inc_id)
            user = incident.users.all()
    
            name = request.session.get("Name")
            cat = request.session.get("Cat_name")
            return render(request, 'backend/search_result.html',{
            'incident_id':inc_id,
            'incident_about':incident.incident_name,
            'incident_details':incident.incident_details,
            'name':name,
            'cat':cat,
            'users':user,
        
            })
        else:
            result = "No Result Found"
            name = request.session.get("Name")
            cat = request.session.get("Cat_name")
            return render(request, 'backend/error_page.html',{
            'name':name,
            'cat':cat,
            'result':result,
            })
    except:
        result = "No Result Found"
        name = request.session.get("Name")
        cat = request.session.get("Cat_name")
        return render(request, 'backend/error_page.html',{
            'name':name,
            'cat':cat,
            'result':result,
            })

                   
@login_required(login_url='login')
def User_Details_page(request,email):
    search_user = User.objects.get(email=email)
    belongs_category = Category.objects.get(id=search_user.category_id)
    
  
    name = request.session.get("Name")
    cat = request.session.get("Cat_name")
    return render(request, 'backend/userDetails.html',{
        'f_name':search_user.first_name,
        'l_name':search_user.last_name,
        'email':search_user.email,
        'phone':search_user.phone_no,
        'std':search_user.std,
        'fax':search_user.fax,
        'mobile':search_user.mobile_no,
        'address':search_user.address,
        'city':search_user.city,
        'state':search_user.state,
        'pincode':search_user.pincode,
        'country':search_user.country,
        'cat_name':belongs_category.name,
        'name':name,
        'cat':cat,})
        

@login_required(login_url='login')
def Edit_Incident_page(request,incident_id):

    inci = Incident.objects.get(incident_id=incident_id)
    inci_name = inci.incident_name
    inci_details = inci.incident_details
    inci_priority = inci.priority
    inci_status = inci.status

    request.session['incident_id'] = incident_id
    name = request.session.get("Name")
    cat = request.session.get("Cat_name")

    return render(request, 'backend/edit_incident.html',{
        'incident_name':inci_name,
        'incident_details':inci_details,
        'incident_priority':inci_priority,
        'incident_status':inci_status,
        'name':name,
        'cat':cat,})

# --------------Handle Dynamic Pages ------------------>
@login_required(login_url='login')
def submitIncidentForm(request):
    try:
        r_date = datetime.now(timezone.utc)
        if request.method == "POST":
            user_id = request.session.get("user_id")
            reporter_name = request.session.get("Name")
            incident_name = request.POST.get('incident_about')
            incident_details = request.POST.get('incident_details')
            incident_priority = request.POST.get('incident_priority')

            incident = Incident.objects.create(
                incident_name=incident_name,
                Reporter_name=reporter_name,
                incident_details=incident_details,
                priority=incident_priority,
                reported_at=r_date,
                status="Open",
            )

            incident.save()
             
            user = User.objects.get(id=user_id)
           
            incident.users.add(user)

            incs = user.incidents.all()

            name = request.session.get("Name")
            cat = request.session.get("Cat_name")
            
            return render(request, 'backend/userDashboard.html',
            {
            'name':name,
            'cat':cat,
            'incidents':incs, 
            })
      
        else:
             result = "Form is not submitted"
        name = request.session.get("Name")
        cat = request.session.get("Cat_name")
        return render(request, 'backend/error_page.html',{
        'name':name,
        'cat':cat,
        'result':result,
        })
        
    except Exception as e:
        print(e)
        
@login_required(login_url='login')
def updateIncidentForm(request):
    try:
        inc_id = request.session.get("incident_id")
        incident = Incident.objects.get(incident_id=inc_id)
        r_date = datetime.now(timezone.utc)
        if request.method == "POST":
            
            incident_name = request.POST.get('incident_about')
            incident_details = request.POST.get('incident_details')
            incident_priority = request.POST.get('incident_priority')
            incident_status = request.POST.get('incident_status')

            incident.incident_name = incident_name
            incident.incident_details = incident_details
            incident.priority = incident_priority
            incident.status = incident_status
            incident.reported_at = r_date
            incident.save()

            messages.success(request, 'Incident updated successfully')
            
            user_id = request.session.get("user_id")
            user = User.objects.get(id=user_id)
            incs = user.incidents.all()

            name = request.session.get("Name")
            cat = request.session.get("Cat_name")
            
            return render(request, 'backend/userDashboard.html',
            {
            'name':name,
            'cat':cat,
            'incidents':incs, 
            })
         
        else:
             result = "Form not updated"
        name = request.session.get("Name")
        cat = request.session.get("Cat_name")
        return render(request, 'backend/error_page.html',{
        'name':name,
        'cat':cat,
        'result':result,
        })
        
    except Exception as e:
        print(e)
         

           
 