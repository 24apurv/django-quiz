from django.http import HttpResponse
from django.shortcuts import render
from .forms import MyUserForm

def login(request):
	form = MyUserForm()
	context = {'form' : form}
	return render(request, 'login.html', context)