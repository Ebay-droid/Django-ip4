from django.db import models
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
# Create your models here.

# class Admin(models.Model):
#   name = models.CharField(max_length=20)
  


class Neighbourhood(models.Model):
  name = models.CharField(max_length=200)
  contacts_health = models.CharField(max_length=200)
  contacts_police =models.CharField(max_length=200)
  # occupants =models.ForeignKey(User,on_delete=models.CASCADE)
  occupants_count =models.IntegerField()
  # admin = models.ForeignKey(Admin,on_delete=models.CASCADE)
  def save_neighbourhood(self):
    self.save()
  
  def delete_neighbourhood(self):
    self.delete()
    
  def find_by_id(self,pk):
    self.objects.get(pk=pk)
    
  
  def __str__(self):
    return self.name        
    
  
class  Occupant(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE,default='',null=True)
  id =models.AutoField(primary_key=True)
  name =models.CharField(max_length=20)
  email =models.EmailField()
  neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)  
  
  def __str__(self):
    return self.name  
  
  
class Business(models.Model) :
  name = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE) 
  
  
  def save_business(self):
    self.save()
  
  def delete_business(self):
    self.delete()
    
  def find_by_id(self,pk):
    self.objects.get(pk=pk)
    
  def __str__(self):
    return self.name  
  
# class  Profile(models.Model):
#   profile_pic = CloudinaryField('image')
#   Bio = models.TextField()
#   email = models.EmailField()
#   phone_number = models.IntegerField(null=True)
#   user = models.ForeignKey(User,on_delete=models.CASCADE,default='')
  
  
#   def __str__(self):
#     return self.user.name
  
#   def save_profile(self):
#     self.save()