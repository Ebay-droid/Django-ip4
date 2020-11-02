from django.shortcuts import render,get_object_or_404,redirect,reverse
from .forms import *
from django.http import  HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import  UserCreationForm
from  django.contrib.auth import login,logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def registerPage(request):
  form = CreateUserForm()
  
  if request.method == 'POST':
    form = CreateUserForm(request.POST)
    if form.is_valid():
      form.save()
      user = form.cleaned_data.get('username')
      messages.success(request,"Account created for" + user)
      return redirect('login')
  
  
  context = {'form':form}
  return render(request,'registration/register.html', context)

def loginPage(request):
  
  if request.method =='POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
      login(request, user)
      return redirect('index')
    else:
      messages.info(request, "The user exists not")
      
  context = {}
  return render (request, 'registration/login.html', context)

def logoutUser(request):
  logout(request)
  return redirect('login')


@login_required(login_url='login')
def index(request):
  return render(request,'index.html')

  

# def update_profile(request, username):
#   user = get_object_or_404(User,username=username)  
#   new_user = request.user
#   if request.method == 'POST':
    
#     form = ProfileForm(request.POST, request.FILES)
#     if form.is_valid():
#       profile = form.save(commit=False)
#       profile.user = new_user
#       profile.save()
      
#       return HttpResponseRedirect(reverse('profile', args=[username]))
#     else:
#       form = ProfileForm()
    
#   return render(request, 'new_profile.html',{'user':user,'form':ProfileForm})   

