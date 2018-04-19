from django import forms

from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)

User = get_user_model()

# Form for User login input

class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget = forms.PasswordInput)
	loginas = forms.CharField()
	
# Form for User Registration Input

class UserRegisterForm(forms.ModelForm):
       class Meta:
	       model=User
	       fields = [
		   'username',
           'first_name',
		   'email',  
		   'password'
		        ]