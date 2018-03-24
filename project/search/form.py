from django import forms
from .models import Posts_of_work,status

class workpost(forms.Form):
	class Meta:
	       model=Posts_of_work
	       fields = [
		   'username',
		   'name',
           'rskill',
		   'start_date',
		   'end_date',
		   'Nworker',
		   'Twork',
		   'description',
		   'status',
		   's_contact',
	       'street',
	       'location',
	       'lat',
	       'lng'
	       ]

