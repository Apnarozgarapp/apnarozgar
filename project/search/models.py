from django.db import models

# Create your models here.
class Posts(models.Model):
	post_id=models.AutoField(primary_key=True)
	username = models.CharField(max_length=100)
	name = models.CharField(max_length = 100,blank = True, null = True)
	s_contact = models.CharField(max_length=50,blank = True,null = True)
	rskill = models.CharField(max_length = 100,blank = True, null = True)
	street = models.CharField(max_length=250,blank = True, null = True)
	location = models.CharField(max_length=250,blank = True, null = True)
	start_date = models.DateField(blank = True, null = True)
	end_date = models.DateField(blank = True, null = True)
	Nworker = models.CharField(max_length=10,blank = True, null = True)
	Twork = models.CharField(max_length = 250,blank = True, null = True)
	description = models.TextField(max_length = 500,blank = True, null = True)
	lat = models.CharField(max_length = 50, blank = True, null= True)
	lng = models.CharField(max_length = 50, blank = True, null= True)
	status = models.CharField(max_length = 50,blank = True, null = True)
	distance = models.FloatField(blank = True, null = True)
	temp=models.CharField(max_length = 2,blank = True, null = True)
	temp1=models.CharField(max_length = 2,blank = True, null = True)
	def __str__(self):
		return self.username
class Status(models.Model):
	status_id=models.AutoField(primary_key=True)
	post_id=models.IntegerField(blank = True, null = True)
	user_id=models.IntegerField(blank = True, null = True)
	hirer = models.CharField(max_length = 100,blank = True, null = True)
	worker = models.CharField(max_length = 100,blank = True, null = True)
	userhirer = models.CharField(max_length = 100,blank = True, null = True)
	userworker = models.CharField(max_length = 100,blank = True, null = True)
	hirer_status = models.IntegerField(blank = True, null = True)
	worker_status = models.IntegerField(blank = True, null = True)
	confirm=models.CharField(max_length = 2,blank = True, null = True)
	temp=models.CharField(max_length = 2,blank = True, null = True)
	start_date = models.DateField(blank = True, null = True)
	end_date = models.DateField(blank = True, null = True)
	done=models.CharField(max_length = 2,blank = True, null = True)

