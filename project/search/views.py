from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib.auth.models import User
from worker.models import Profile,location
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django import forms
import re
import urllib.request
from math import sin, cos, sqrt, atan2, radians
from django.db.models import Q

@login_required
@transaction.atomic

def search_result(request):
  if request.method == 'POST':
    skill = request.POST.get('skill',None)
    s_date = request.POST.get('start_date',None)
    e_date = request.POST.get('end_date',None)
    address = request.POST.get('address',None)
    salary = request.POST.get('salary',None)
    lat1 = request.POST.get('lat',None)
    lng1 = request.POST.get('lng',None)
    
    try :
      user1=Profile.objects.filter(Q(skill1=skill)|Q(skill2=skill)|Q(skill3=skill))    
      user1 = user1.filter(start_date__lte=s_date,end_date__gte=e_date,min_salary__lte=salary)
      for data in user1:
        loc=location.objects.get(username=data.user.username)
        dis=discal(float(lat1),float(lng1),float(loc.lat),float(loc.lng))
        print(dis)
        data.age=dis
        data.save()
      user1=user1.order_by('age')
      if len(user1) == 0:
        warn = "आपकी आवश्यकता से मेल खाने वाला कोई परिणाम नहीं है|"
      else:
        warn = ""
      return render(request,'search/result.html',{'users' : user1, 'warn' : warn})
    except Profile.DoesNotExist:
      return HttpResponse(" No Worker available.")  
  else:
   
      return render(request,'search/search.html')

def discal(a,b,c,d):
  R = 6373.0
  lat1 = radians(a)
  lon1 = radians(b)
  lat2 = radians(c)
  lon2 = radians(d)

  dlon = lon2 - lon1
  dlat = lat2 - lat1

  a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
  c = 2 * atan2(sqrt(a), sqrt(1 - a))

  distance = R * c
  return round(distance,2)
def view_worker(request):
  if request.method == 'GET':
    dat = request.GET['data']
    data= Profile.objects.get(  user_id= dat)
    return render(request,'worker/view.html',{'data': data})  
  else:
    return HttpResponse(" No Worker available.") 