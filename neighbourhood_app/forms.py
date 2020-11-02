from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# class ProfileForm(forms.ModelForm):
#   class Meta:
#     model = Profile
#     exclude = ['user']    
    
    
class  CreateUserForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username','email','password1','password2']    