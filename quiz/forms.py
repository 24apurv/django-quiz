from .models import MyUser
from django.forms import ModelForm

class MyUserForm(ModelForm):
	class Meta:
		model = MyUser
		fields = ['name_1', 'email_1', 'phone_number_1', 'name_2', 'email_2', 'phone_number_2', 'team_name']