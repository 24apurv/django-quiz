from django.http import HttpResponse
from django.shortcuts import render
from .forms import MyUserForm
from django.contrib import messages

def login(request):
	form = MyUserForm(request.POST or None)
	if request.method == 'POST' :
		if form.is_valid():
			user = form.save()
			request.session['user_id'] = user.id
			messages.success(request, 'User logged in - {}'.format(user.id))
			return render(request, 'login.html')
	else:	
		context = {'form' : form}
		return render(request, 'login.html', context)