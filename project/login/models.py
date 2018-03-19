from django.db import models

# Create your models here.
class LoginAs(models.Model):
    username = models.CharField(max_length=50,primary_key = True)
    loginas = models.CharField(max_length=50, null = True)
    def __str__(self):
    	return self.username
class Registration_otp(models.Model):
    username = models.CharField(max_length=15,primary_key = True)
    otp = models.CharField(max_length=5)
    def __str__(self):
    	return self.username

