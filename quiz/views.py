from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Answer, Question, Result, MyUser
from .forms import MyUserForm, QuizForm
from django.contrib import messages
from django.conf import settings 

def login(request):
	flag = False
	if request.method == 'POST' :
		form = MyUserForm(request.POST, request.FILES)
		if form.is_valid():
			user = form.save()
			flag = True
	if flag:
		return redirect('instructions', user.id)
	else:
		form = MyUserForm()
		context = {'form' : form}
		return render(request, 'login.html', context)


def take_quiz(request, user_id=None):
	try:
		user = MyUser.objects.get(pk=user_id)
	except:
		return redirect('login')
	questions = Answer.objects.all()
	questions.order_by('?')
	form = QuizForm(request.POST or None, questions=questions)
	flag = False
	if request.method == 'POST':
		if form.is_valid():
			score = 0
			for (quiz_question, answer) in form.answers():
				question = Question.objects.get(statement=quiz_question)
				correct_answer = Answer.objects.get(question=question).correct_answer
				if answer == correct_answer:
					score = score+1
			result = Result(user=user, score=score)
			result.save()
			flag = True
	if flag:
		return redirect('finish')
	content = zip(questions, form)
	context = {'content':content}
	return render(request, 'quiz.html', context)


def instructions(request, user_id=None):
	try:
		user = MyUser.objects.get(pk=user_id)
	except:
		return redirect('login')
	if request.method == 'POST':
		return redirect('take_quiz', user.id)
	instructions = [
	'You have 30 mins to solve all problems',
	'Do not close or refresh the quiz window',
	'There will be 30 questions carrying 1 mark each',
	]
	context = {'instructions':instructions, 'time':1}
	return render(request, 'instructions.html', context)


def finish(request):
	if request.method == 'POST':
		return redirect('login')
	return render(request, 'finish.html') 

