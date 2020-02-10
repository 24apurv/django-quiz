from .models import MyUser
from django.forms import ModelForm
from django import forms
from django.forms import widgets

class MyUserForm(ModelForm):
	class Meta:
		model = MyUser
		fields = ['name_1', 'email_1', 'phone_number_1', 'name_2', 'email_2', 'phone_number_2', 'team_name']


class QuizForm(forms.Form):

	def __init__(self, *args, **kwargs):
		questions = kwargs.pop('questions')
		super().__init__(*args, **kwargs)
		for i, question in enumerate(questions):
			CHOICES = [
				('a', question.option_a),
				('b', question.option_b), 
				('c', question.option_c),
				('d', question.option_d),
			]
			self.fields[question.question.statement] = forms.ChoiceField(choices=CHOICES, widget=widgets.RadioSelect)

	def answers(self):
		for name, question in self.cleaned_data.items():
			if name.startswith('question_'):
				yield(self.fields[name].label, value)