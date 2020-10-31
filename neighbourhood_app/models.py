from django.db import models
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
# Create your models here.


class Neighbourhood(models.Model):
  name = models.CharField(max_length=200)
  contacts_health = models.CharField(max_length=200)
  contacts_police =models.CharField(max_length=200)
  
  
class Business(models.Model) :
  name = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE) 
  
  
class  Profile(models.Model):
  profile_pic = CloudinaryField('image')
  Bio = models.TextField()
  email = models.EmailField()
  phone_number = models.IntegerField(null=True)
  user = models.ForeignKey(User,on_delete=models.CASCADE,default='')
  neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)  