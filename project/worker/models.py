from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime, timedelta

#table to store the profile of worker and contractor
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True) #to link each user with a profile
    s_contact = models.CharField(max_length=50,blank = True,null = True) #mobile number
    gender = models.CharField(max_length=10,blank = True,null = True) 
    dis = models.FloatField(blank = True, null = True) #variable that stores the distance between the worker and the hirer searching him at that time
    street = models.CharField(max_length=250,blank = True, null = True) #locality address
    address = models.CharField(max_length=250,blank = True, null = True) #complete Google address
    start_date = models.DateField(blank = True, null = True) #start_date of work availability
    end_date = models.DateField(blank = True, null = True) #end_date of work availability
    skill1 = models.CharField(max_length = 100,blank = True, null = True) #skills of the worker
    skill2 = models.CharField(max_length = 100,blank = True, null = True)
    skill3 = models.CharField(max_length = 100,blank = True, null = True)
    description1 = models.TextField(max_length = 250,blank = True, null = True)#description about skills
    description2 = models.TextField(max_length = 250,blank = True, null = True)
    description3 = models.TextField(max_length = 250,blank = True, null = True)
    description = models.TextField(max_length = 500,blank = True, null = True)
    description11 = models.TextField(max_length = 250,blank = True, null = True)
    min_salary = models.IntegerField(blank = True, null = True) #minimum salary that the worker demands
    rating = models.FloatField(blank = True, null = True) #average rating received by worker
    nhirer = models.IntegerField(blank = True, null = True) # number of hirers who have rated the worker till now
    loginas = models.TextField(max_length = 10,blank = True, null = True) #login role (hirer/contractor/worker)
    joinrequest=models.CharField(max_length = 2,blank = True, null = True) # variable to store the status of work request between hirer and contractor
    temp=models.CharField(max_length = 2,blank = True, null = True) # temporary variable
    ac = models.CharField(max_length=100,blank = True, null = True) # Account details (A/c number)
    ifsc = models.CharField(max_length=100,blank = True, null = True) #ifsc
    paytm = models.CharField(max_length=100,blank = True, null = True)# paytm number
    upi = models.CharField(max_length=100,blank = True, null = True)#upi id
    acname = models.CharField(max_length=100,blank = True, null = True) #a/c holder name
    bank = models.CharField(max_length=100,blank = True, null = True) #bank name
    mode = models.CharField(max_length=100,blank = True, null = True)#mode of payment desired
    contractor=models.PositiveSmallIntegerField(blank = True, null = True,default=0) #number of skills provided by contractor

    
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
    lat = models.CharField(max_length = 50, blank = True, null= True) #latitude
    lng = models.CharField(max_length = 50, blank = True, null= True) #longitude
    def __str__(self):
        return self.username

class Current_location(models.Model):
    username = models.CharField(max_length = 50, primary_key = True)
    address = models.CharField(max_length=250,blank = True, null = True) # current address 
    lat = models.CharField(max_length = 50, blank = True, null= True) # current coordinates
    lng = models.CharField(max_length = 50, blank = True, null= True)
    time = models.CharField(max_length = 50, blank = True, null= True) # time of recording current address
    def __str__(self):
        return self.username
    
class Contractor(models.Model):
    cid=models.AutoField(primary_key=True) # contractor Id
    user=models.ForeignKey(User,on_delete=models.CASCADE) #link to USER table
    skill= models.CharField(max_length=100,blank = True,null = True) #skill of the contractor (a separate table for each skill)
    nofworker = models.IntegerField(blank = True, null = True) #number of workers that contractor has for that skill
    nameof_worker = models.CharField(max_length=1024,blank = True, null = True) #name of workers above 
    equipment = models.CharField(max_length=250,blank = True, null = True) #equipments possessed by contractor
    start_date = models.DateField(blank = True, null = True) #start date of availabaility
    end_date = models.DateField(blank = True, null = True) # end date of availabaility
    experience = models.CharField(max_length = 250, blank = True, null= True) # experience with skills
    description1 = models.TextField(max_length = 250,blank = True, null = True)# descriptions about skills
    description2 = models.TextField(max_length = 100,blank = True, null = True) 
    dis = models.FloatField(blank = True, null = True) #variable that stores the distance between the contractor and the hirer searching him at that time
    joinrequest=models.CharField(max_length = 2,blank = True, null = True)# variable to store the status of work request between hirer and contractor
    def __str__(self):
        return self.user.username
