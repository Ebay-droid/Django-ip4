from  django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('user/<username>/', views.user_profile, name='user_profile'),
    path('hood/<int:id>/', views.hood_details, name='hood'),
    path('profile/<username>/',views.profile, name='profile'),
    path('welcome/',views.welcome, name='welcome'),
    # path('hoods/',views.hoods, name='all_hoods'),
    # path('join_hood/<int:id>',views.join_neighbourhood, name='join_hood'),
    
    
]