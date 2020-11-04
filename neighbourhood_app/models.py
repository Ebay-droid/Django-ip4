from django.db import models
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
# Create your models here.

  


class Neighbourhood(models.Model):
  CHOICES = (
    (' Kikuyu ', 'Kikuyu'),
    ('Dago', 'Dagoretti'),
    ('Karen', 'Karen'),
    ('Kabete', 'Kabete'),
    ('Kasarani', 'Kasarani'),
    ('Rongai', 'Rongai'),
    ('Westie', 'Westland'),
    ('Parkie', 'Parkland'),
  )
  name = models.CharField(max_length=200,choices=CHOICES)
  location = models.CharField(max_length=200, default='Kenya')
  occupants_count =models.IntegerField(default=0)
  admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_name', default=1)
  def save_neighbourhood(self):
    self.save()
  
  def delete_neighbourhood(self):
    self.delete()
    
  def find_by_id(self,pk):
    hood =self.objects.get(pk=pk)
    return Neighbourhood.objects.filter(name=hood)
  
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
    biz = self.objects.get(pk=pk)
    return Business.objects.filter(name=biz)
    
    
  def __str__(self):
    return self.name  
  
  @classmethod
  def search_business(cls,search_term):
      biz = Business.objects.filter(name__icontains=search_term)
      return biz
  
class  Profile(models.Model):
  profile_pic = CloudinaryField('image')
  Bio = models.TextField()
  phone_number = models.IntegerField(null=True)
  user = models.ForeignKey(User,on_delete=models.CASCADE, )
  neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE,)  

  
  def __str__(self):
    return self.user.username
  
  def save_profile(self):
    self.save()
    
    
class Post(models.Model):
  post = models.CharField(max_length=300)
  neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE,)    
  image = CloudinaryField('images')
  profile = models.ForeignKey(Profile,on_delete=models.CASCADE,default='')


  def __str__(self):
    return self.user.username
  