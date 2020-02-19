from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Answer, Question, MyUser, UserAnswer
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
	c_questions = Question.objects.filter(category='C').order_by('?')[0:10]
	cpp_questions = Question.objects.filter(category='C++').order_by('?')[0:10]
	questions_obj = c_questions | cpp_questions
	id_list = []
	if request.session.get('questions'):
		id_list = request.session['questions']
	else:
		for question_obj in questions_obj:
			id_list.append(question_obj.id)
	questions = Answer.objects.filter(question_id__in=id_list)
	form = QuizForm(request.POST or None, questions=questions)
	flag = False
	if request.method == 'POST':
		if form.is_valid():
			questions_list = []
			answers_list = []
			for (quiz_question, answer) in form.answers():
				questions_list.append(quiz_question)
				answers_list.append(answer)
			user_answers = UserAnswer(user=user, questions=','.join(questions_list), answers=','.join(answers_list))
			user_answers.save()
			flag = True
	if flag:
		request.session.clear()
		return redirect('finish')
	content = zip(questions, form)
	request.session['questions'] = id_list
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

