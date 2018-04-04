from django.db import models

# Create your models here.
class LoginAs(models.Model):
    username = models.CharField(max_length=100,primary_key = True)
    loginas = models.CharField(max_length=50, null = True)
    def __str__(self):
    	return self.username
class Registration_otp(models.Model):
    username = models.CharField(max_length=100,primary_key = True)
    aadhar = models.CharField(max_length=12)
    otp = models.CharField(max_length=5)
    def __str__(self):
    	return self.otp

class Feedback(models.Model):
    feedback_id=models.AutoField(primary_key=True)
    userhirer = models.CharField(max_length=100,blank = True, null = True)
    userworker = models.CharField(max_length=100,blank = True, null = True)
    post_id=models.IntegerField(blank = True, null = True)
    feedback1=models.TextField(max_length = 100,blank = True, null = True)
    feedback2=models.TextField(max_length = 100,blank = True, null = True)
    feedback3=models.TextField(max_length = 100,blank = True, null = True)
    description=models.TextField(max_length = 200,blank = True, null = True)
    pmode = models.CharField(max_length = 2,blank = True, null = True)
    pdate = models.DateField(blank = True, null = True)

