from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .models import Reg
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from .forms import CreateUserForm

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *


def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'accounts/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

def home(request):
	return render(request, 'accounts/dashboard.html')
def course(request):
	return render(request,'accounts/course.html')

def reg(request):
	if request.user.is_authenticated:

		if request.method=='POST':
			schoolmark=request.POST['schoolmark']
			print(schoolmark)
			highschoolmark=request.POST['highschoolmark']
			collegename=request.POST['collegename']
			cgpa=request.POST['cgpa']
			aadharno=request.POST['aadharno']
			phoneno=request.POST['phoneno']
			address=request.POST['address']
			myuser=Reg(schoolmark=schoolmark,highschoolmark=highschoolmark,collegename=collegename,cgpa=cgpa,aadharno=aadharno,phoneno=phoneno,address=address)
			myuser.save()
			messages.success(request, "message send success fully>>>>>>>")
			return redirect('fpage')
			print('sucess')
	return render(request,'accounts/reg.html')	 

def fpage(request):
	return render(request, "accounts/fpage.html")

