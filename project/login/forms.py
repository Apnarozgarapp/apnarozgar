from django import forms

from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)

User = get_user_model()

class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget = forms.PasswordInput)
	loginas = forms.CharField()
	

class UserRegisterForm(forms.ModelForm):
       class Meta:
	       model=User
	       fields = [
		   'username',
           'first_name',
           'last_name',
		   'email',  
		   'password'
		        ]