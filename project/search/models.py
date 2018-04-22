from django.db import models

# table to store every post created
class Posts(models.Model):
	post_id=models.AutoField(primary_key=True) 
	username = models.CharField(max_length=100) # hirer who created the post
	name = models.CharField(max_length = 100,blank = True, null = True) #name of the hirer
	s_contact = models.CharField(max_length=50,blank = True,null = True)# mobile number
	rskill = models.CharField(max_length = 100,blank = True, null = True) # skill required for the work post
	street = models.CharField(max_length=250,blank = True, null = True)#locality
	location = models.CharField(max_length=250,blank = True, null = True)#google location of work site
	start_date = models.DateField(blank = True, null = True)# dates of work
	end_date = models.DateField(blank = True, null = True)
	Nworker = models.CharField(max_length=10,blank = True, null = True) # no. of workers required
	Twork = models.CharField(max_length = 250,blank = True, null = True) #type of payment(daily/monthly/hourly)
	description = models.TextField(max_length = 500,blank = True, null = True) # description of work
	lat = models.CharField(max_length = 50, blank = True, null= True)# coordinates of work location
	lng = models.CharField(max_length = 50, blank = True, null= True)
	status = models.CharField(max_length = 50,blank = True, null = True) #variable to store status of work request between hirer and worker
	distance = models.FloatField(blank = True, null = True) #distance between worker and work location
	temp=models.CharField(max_length = 2,blank = True, null = True) #temporary variable
	target=models.CharField(max_length = 2,blank = True, null = True) #target of the post (worker/contractor)
	def __str__(self):
		return self.username

	# to store the status of each post for a worker/contractor	
class Status(models.Model):
	status_id=models.AutoField(primary_key=True) 
	post_id=models.IntegerField(blank = True, null = True) 
	user_id=models.IntegerField(blank = True, null = True)
	hirer = models.CharField(max_length = 100,blank = True, null = True) #name of the hirer
	worker = models.CharField(max_length = 100,blank = True, null = True) #name of worker/contractor
	userhirer = models.CharField(max_length = 100,blank = True, null = True)#username of the hirer
	userworker = models.CharField(max_length = 100,blank = True, null = True) #username of worker/contractor
	hirer_status = models.IntegerField(blank = True, null = True) #status of work request w.r.t hirer
	worker_status = models.IntegerField(blank = True, null = True) #status of work request w.r.t worker/contractor
	confirm=models.CharField(max_length = 2,blank = True, null = True) # variable to store whether there is confirmation between hirer and worker or not 
	temp=models.CharField(max_length = 2,blank = True, null = True) #temporary variable
	start_date = models.DateField(blank = True, null = True) # dates of the work
	end_date = models.DateField(blank = True, null = True)
	done=models.CharField(max_length = 2,blank = True, null = True)# whether the hirer has given payment and review
	target=models.CharField(max_length = 2,blank = True, null = True)# target of the post (hirer/worker)

