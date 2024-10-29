from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':"name@example.com"}),required=True)
    password1 = forms.PasswordInput(attrs={'placeholder':"Enter Password"})
    password2 = forms.PasswordInput(attrs={'placeholder':"Enter Password Again"})
     

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':"name@example.com"}),required=True)
    password = forms.PasswordInput(attrs={'placeholder':"Enter Password"})
    class Meta:
        model = User
        fields = ['email', 'password']

class UserForm(forms.ModelForm):
    f_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"First Name"}),required=True)
    l_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Last Name"}),required=True)
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Last Name"}),required=True)
    country = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Last Name"}),required=True)

    STATE_CHOICES = [
        ('Select', 'Select'),
        ('Agra', 'Agra'),
        ('Banglore', 'Banglore'),
        ('Chandigarh', 'Chandigarh'),
        ('Chennai', 'Chennai'),
        ('Delhi', 'Delhi'),
        ('Gurugram', 'Gurugram'),
        ('Hyderabad', 'Hyderabad'),
        ('Kolkata', 'Kolkata'),
         ('Mathura', 'Mathura'),
        ('Mumbai', 'Mumbai'),
        ('Noida', 'Noida'),
        ('Pune', 'Pune'),
   
    ]
    state = forms.ChoiceField(choices=STATE_CHOICES, widget=forms.Select(attrs={'placeholder': 'Select State'}),required=True)
    city = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"City"}),required=True)
    pincode = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':"Pincode"}),required=True) 
    std = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"STD Code"}),required=True)
    mobile_no = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':"WhatsApp Mobile Number"}),required=True)
    fax = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':"011-55541234"}),required=True)
    phone_no = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':"011-55541234"}),required=True)
    

    class Meta:
        model = User
        fields = ['f_name', 'l_name', 'std', 'phone_no', 'fax', 'mobile_no', 'address', 'pincode', 'city', 'state', 'country']        