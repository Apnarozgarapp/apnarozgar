from django import forms
from django.contrib.auth.models import User
from .models import Profile
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'last_name')

class ProfileForm1(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('s_contact','street','address', 'start_date','end_date')

class ProfileForm2(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('skill1','skill2','skill3','description','min_salary')

