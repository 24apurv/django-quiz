from django.db import models
from django.core.validators import RegexValidator
from django import forms
from django.contrib import admin

#Model for user ie. participant
class MyUser(models.Model):
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be valid")
	name_1 = models.CharField(max_length=100, verbose_name='Participant 1 Name')
	email_1 = models.EmailField(unique=True, verbose_name='Participant 1 Email')
	phone_number_1 = models.CharField(validators=[phone_regex], max_length=17, blank=False, verbose_name='Participant 1 Phone Number')
	name_2 = models.CharField(max_length=100, null=True, blank=True, verbose_name='Participant 2 Name')
	email_2 = models.EmailField(unique=True, null=True, blank=True, verbose_name='Participant 2 Email')
	phone_number_2 = models.CharField(validators=[phone_regex], max_length=17, blank=True, verbose_name='Participant 2 Phone Number')
	team_name = models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		if self.team_name:
			return self.team_name
		else:
			return self.name_1

#Model for question
class Question(models.Model):
	CATEGORY_CHOICES = [('C++','C++'),('C','C')]

	statement = models.CharField(max_length=700, verbose_name='Question statement')
	is_active = models.BooleanField(default=True, verbose_name='Active', help_text='Should question be included in quiz?')
	img = models.ImageField(upload_to='images/', null=True, blank=True)
	has_image = models.BooleanField(default=False, verbose_name='Image', help_text='Does question have image?')
	category = models.CharField(max_length=5, default='C++', verbose_name='Category', choices=CATEGORY_CHOICES)

	def __str__(self):
		return self.statement

class AdminQuestion(admin.ModelAdmin):
	formfield_overrides = {
		models.CharField: {'widget': forms.Textarea},
    }


ANSWER_CHOICES = [
	('A','A'),
	('B','B'),
	('C','C'),
	('D','D'),
	]	
#Model for Answer which contains options and foreign ket to question 
class Answer(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	option_a = models.CharField(max_length=500, blank=False, null=False, verbose_name='Option A')
	option_b = models.CharField(max_length=500, blank=False, null=False, verbose_name='Option B')
	option_c = models.CharField(max_length=500, blank=False, null=False, verbose_name='Option C')
	option_d = models.CharField(max_length=500, blank=False, null=False, verbose_name='Option D')
	correct_answer = models.CharField(max_length=2, blank=False, null=False, choices=ANSWER_CHOICES)

	def __str__(self):
		return self.question.statement

#Model to store answers given by participant. Stored in the form of comma-separated string
class UserAnswer(models.Model):
	user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
	questions = models.CharField(max_length=500, null=True, blank=True)
	answers = models.CharField(max_length=500, null=True, blank=True)

	def __str__(self):
		return str(self.user)

