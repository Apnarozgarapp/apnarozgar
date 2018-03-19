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
	#def clean(self,*args,**kwargs):
	#	username = self.cleaned_data.get("username")
	#	password = self.cleaned_data.get("password")
	#	user = authenticate(username = username,password = password)
	#	if not user:
	#		raise forms.ValidationError("This user does not exist.")
	#	if not user.check_password(password):
	#		raise forms.ValidationError("The password is incorrect.")
	#	if not user.is_active:
	#		raise forms.ValidationError("This user is not active")
	#	return super(UserLoginForm,self).clean(*args,**kwargs)

class UserRegisterForm(forms.ModelForm):
       class Meta:
	       model=User
	       fields = [
		   'username',
           'first_name',
		   'email',  
		   'password'
		        ]