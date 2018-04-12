from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime, timedelta

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
    s_contact = models.CharField(max_length=50,blank = True,null = True)
    dis = models.FloatField(blank = True, null = True)
    street = models.CharField(max_length=250,blank = True, null = True)
    address = models.CharField(max_length=250,blank = True, null = True)
    start_date = models.DateField(blank = True, null = True)
    end_date = models.DateField(blank = True, null = True)
    skill1 = models.CharField(max_length = 100,blank = True, null = True)
    skill2 = models.CharField(max_length = 100,blank = True, null = True)
    skill3 = models.CharField(max_length = 100,blank = True, null = True)
    description1 = models.TextField(max_length = 250,blank = True, null = True)
    description2 = models.TextField(max_length = 250,blank = True, null = True)
    description3 = models.TextField(max_length = 250,blank = True, null = True)
    description = models.TextField(max_length = 500,blank = True, null = True)
    description11 = models.TextField(max_length = 250,blank = True, null = True)
    min_salary = models.IntegerField(blank = True, null = True)
    rating = models.FloatField(blank = True, null = True)
    nhirer = models.IntegerField(blank = True, null = True)
    loginas = models.TextField(max_length = 10,blank = True, null = True)
    joinrequest=models.CharField(max_length = 2,blank = True, null = True)
    temp=models.CharField(max_length = 2,blank = True, null = True)
    ac = models.CharField(max_length=100,blank = True, null = True)
    ifsc = models.CharField(max_length=100,blank = True, null = True)
    paytm = models.CharField(max_length=100,blank = True, null = True)
    upi = models.CharField(max_length=100,blank = True, null = True)
    acname = models.CharField(max_length=100,blank = True, null = True)
    bank = models.CharField(max_length=100,blank = True, null = True)
    mode = models.CharField(max_length=100,blank = True, null = True)
    contractor=models.PositiveSmallIntegerField(blank = True, null = True,default=0)

    
    def __str__(self):
    	return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, **kwargs):
#    instance.profile.save()

post_save.connect(create_user_profile, sender=User)

class location(models.Model):
    username = models.CharField(max_length = 50, primary_key = True)
    lat = models.CharField(max_length = 50, blank = True, null= True)
    lng = models.CharField(max_length = 50, blank = True, null= True)
    def __str__(self):
        return self.username

class Current_location(models.Model):
    username = models.CharField(max_length = 50, primary_key = True)
    address = models.CharField(max_length=250,blank = True, null = True)
    lat = models.CharField(max_length = 50, blank = True, null= True)
    lng = models.CharField(max_length = 50, blank = True, null= True)
    time = models.CharField(max_length = 50, blank = True, null= True)
    def __str__(self):
        return self.username
    
class Contractor(models.Model):
    cid=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    skill= models.CharField(max_length=100,blank = True,null = True)
    nofworker = models.IntegerField(blank = True, null = True)
    nameof_worker = models.CharField(max_length=1024,blank = True, null = True)
    equipment = models.CharField(max_length=250,blank = True, null = True)
    start_date = models.DateField(blank = True, null = True)
    end_date = models.DateField(blank = True, null = True)
    experience = models.CharField(max_length = 250, blank = True, null= True)
    description1 = models.TextField(max_length = 250,blank = True, null = True)
    description2 = models.TextField(max_length = 100,blank = True, null = True)
    dis = models.FloatField(blank = True, null = True)
    joinrequest=models.CharField(max_length = 2,blank = True, null = True)
    def __str__(self):
        return self.user.username
