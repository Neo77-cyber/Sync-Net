from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



# creating a form
class InputForm(forms.Form):

	first_name = forms.CharField(max_length = 200)
	last_name = forms.CharField(max_length = 200)
	password = forms.CharField(widget = forms.PasswordInput())
