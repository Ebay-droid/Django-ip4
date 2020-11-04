from django.shortcuts import render,get_object_or_404,redirect,reverse
from .forms import *
from django.http import  HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import  UserCreationForm
from  django.contrib.auth import login,logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import Group,User
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user,allowed_user
# Create your views here.
@unauthenticated_user
def registerPage(request):
  form = CreateUserForm()
  
  if request.method == 'POST':
    form = CreateUserForm(request.POST)
    if form.is_valid():
      user = form.save()
      username = form.cleaned_data.get('username')
      
      group = Group.objects.get(name = "user")
      user.groups.add(group)
      
      messages.success(request,"Account created for" + username)
      return redirect('login')
  
  
  context = {'form':form}
  return render(request,'registration/register.html', context)


@unauthenticated_user
def loginPage(request):
  
  if request.method =='POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
      login(request, user)
      return HttpResponseRedirect(reverse('user_profile', args=[username]))
    else:
      messages.info(request, "The user exists not")
      
  context = {}
  return render (request, 'registration/login.html', context)

def logoutUser(request):
  logout(request)
  return redirect('login')


# @unauthenticated_user
# @allowed_user(allowed_roles=['__all__'])
@login_required(login_url='login')
def index(request):
  neighbourhood = Neighbourhood.objects.all()
  
  return render(request,'index.html',{'hood':neighbourhood})


@login_required(login_url='login')
# @allowed_user(allowed_roles=['user'])
  
def user_profile(request, username):
  user = get_object_or_404(User,username=username)  
  new_user = request.user
  if request.method == 'POST':
    
    form = ProfileForm(request.POST, request.FILES)
    if form.is_valid():
      profile = form.save(commit=False)
      profile.user = new_user
      profile.save()
      
      # return redirect(request,'profile.html')
      return HttpResponseRedirect(reverse('profile.html', args=[username]))
    else:
      form = ProfileForm()
    
  return render(request, 'new_profile.html',{'user':user,'form':ProfileForm})   

@login_required(login_url='login')
# @allowed_user(allowed_roles=['user','admin'])
def hood_details(request):
  neighbourhood = Neighbourhood.objects.all()
  
  return render (request, 'neighbourhood_details.html',{'hood':neighbourhood})
  
@login_required  
def profile(request,username):
  user = get_object_or_404(User,username=username)
  profile = Profile.objects.get(user=user)

  
  return render(request, 'profile.html',{'user':user,'profile':profile}) 


