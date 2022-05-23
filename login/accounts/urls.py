from django.urls import path
from . import views


urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('', views.home, name="home"),
	path('course/',views.course,name="course"),
    path('fpage/',views.fpage,name="fpage"),
	path('reg/',views.reg,name="reg"),

    
  

]