from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Answer, Question, Result, MyUser
from .forms import MyUserForm
from django.contrib import messages

def login(request):
	flag = False
	form = MyUserForm(request.POST or None)
	if request.method == 'POST' :
		if form.is_valid():
			user = form.save()
			flag = True
	if flag:
		return redirect('take_quiz', user.id)
	else:	
		context = {'form' : form}
		return render(request, 'login.html', context)


def take_quiz(request, user_id=None):
	try:
		user = MyUser.objects.get(pk=user_id)
	except:
		return redirect('login')
	questions = Answer.objects.all()
	context = {'questions' : questions}
	return render(request, 'quiz.html', context)
