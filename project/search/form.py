from django import forms

class workersearchForm(forms.Form):
	username = forms.CharField(label='username')
	skills = forms.CharField(label='skills')

	#skills = forms.ChoiceField(choices=('a','b','c'), label='skills')

