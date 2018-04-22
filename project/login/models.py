from django.db import models

# Create your models here.

    	

# Table to store otp and aadhar with username at the time of Registration, forgot Password and change Password

class Registration_otp(models.Model):
    username = models.CharField(max_length=100,primary_key = True)
    aadhar = models.CharField(max_length=12)
    otp = models.CharField(max_length=5)
    def __str__(self):
    	return self.username

# Table to store Feedback details and Payment for Workers or Contractors

class Feedback(models.Model):
    feedback_id=models.AutoField(primary_key=True)
    userhirer = models.CharField(max_length=100,blank = True, null = True)  #username of hirer 
    userworker = models.CharField(max_length=100,blank = True, null = True) #username of worker
    post_id=models.IntegerField(blank = True, null = True)                  #ID of  Work Post 
    feedback1=models.TextField(max_length = 100,blank = True, null = True)  #Feedback Detail fields 
    feedback2=models.TextField(max_length = 100,blank = True, null = True)
    feedback3=models.TextField(max_length = 100,blank = True, null = True)
    description=models.TextField(max_length = 200,blank = True, null = True)
    pmode = models.CharField(max_length = 50,blank = True, null = True)       #Mode of payment by Hirer to Worker
    pdate = models.DateField(blank = True, null = True)                      #Payment Date
    done=models.CharField(max_length = 2,blank = True, null = True)          # variable to check status of payment verification ("a" if payment not verified by worker, "b" otherwise)
    target=models.CharField(max_length = 2,blank = True, null = True)        # whether feedback data target is worker or Contractor

