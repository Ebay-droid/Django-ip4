from django.test import TestCase
from .models import  *
from django.contrib.auth.models import User
# Create your tests here.
class  ProfileTest(TestCase):
  def setUp(self):
    user = User.objects.create(username='test',password = 'hood')
    self.test = Profile(Bio='woohoo',user=user)
    
  def test_instance(self):
    self.assertTrue(isinstance(self.test,Profile))


class NeighbourhoodTest(TestCase):
  def setUp(self):
    user = User.objects.create(username='test',password = 'hood')
    self.test = Neighbourhood(name='Kabete',location='KENYA',occupants_count=20,admin=user,contact_police=999,contact_health=526325,contact_fire=02202522)
  
  def test_instance(self):
    self.assertTrue(isinstance(self.test,Neighbourhood))  

  def test_save(self):
    self.test.save_neighbourhood()
    saved = Neighbourhood.objects.all()
    self.assertTrue(len(saved)>0)
    
    
  def test_delete(self):
    self.test.save_neighbourhood()
    self.test.delete_neighbourhood()
    deleted = Neighbourhood.objects.all()
    self.assertTrue(len(deleted)== 0) 
    
    
  def test_find_by_id(self):
    self.test.sa  

  # def tearDown(self):
  #   Project.objects.all().delete()