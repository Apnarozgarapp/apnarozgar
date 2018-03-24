from django.db import models

# Create your models here.
class Posts_of_work(models.Model):
	username = models.CharField(max_length=100,primary_key = True)
	s_contact = models.CharField(max_length=50,blank = True,null = True)
	rskill = models.CharField(max_length = 100,blank = True, null = True)
	street = models.CharField(max_length=250,blank = True, null = True)
	location = models.CharField(max_length=250,blank = True, null = True)
	start_date = models.DateField(blank = True, null = True)
	end_date = models.DateField(blank = True, null = True)
	Nworker = models.IntegerField(blank = True, null = True)
	Twork = models.CharField(max_length = 250,blank = True, null = True)
	description = models.TextField(max_length = 500,blank = True, null = True)
	lat = models.CharField(max_length = 50, blank = True, null= True)
	lng = models.CharField(max_length = 50, blank = True, null= True)
	status = models.CharField(max_length = 50,blank = True, null = True)
	def __str__(self):
		return self.username
class status(models.Model):
	postid=models.IntegerField(blank = True, null = True)
	worker = models.CharField(max_length = 100,blank = True, null = True)
	hirer_status = models.CharField(max_length = 10,blank = True, null = True)
	worker_status = models.CharField(max_length = 10,blank = True, null = True)
	def __str__(self):
		return self.postid