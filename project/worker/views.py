from django.shortcuts import render
from .forms import  ProfileForm1,ProfileForm2
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib.auth.models import User
from .models import Profile,location
from search.models import Posts
import login
import re
import urllib.request
from django.db.models import Q
from math import sin, cos, sqrt, atan2, radians
import datetime
@login_required
@transaction.atomic

def update_profile(request):
  
    if request.method == 'POST' and 'save_changes1' in request.POST:
        profile_form = ProfileForm1(request.POST, instance=request.user.profile)
        lat=request.POST.get('lat')
        lng=request.POST.get('lng')
        if profile_form.is_valid():
            profile_form.save()
            if lat != '0':
	            da=location(username=request.user.username,lat=lat,lng=lng)
	            da.save()
            return render(request,'worker/worker2.html')
        else:
          warn ="Correct the details."
          return render(request,'worker/worker1.html',{"warn":warn})
    if request.method == 'POST' and 'save_changes2' in request.POST:
      profile_form = ProfileForm2(request.POST, instance=request.user.profile)
      if profile_form.is_valid():
         profile_form.save()
         return render(request,'worker/success.html')
      else:
          warn ="Correct the details."
          return render(request,'worker/worker2.html',{"warn":warn})
    else:
       return render(request,'worker/worker1.html')

def view_profile(request):
    return render(request,'worker/view.html')

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

def viewpost(request):
  data=Profile.objects.get(user=request.user)
  pos=Posts.objects.filter(Q(rskill=data.skill1)|Q(rskill=data.skill2)|Q(rskill=data.skill3))
  pos=pos.filter(status='public')
  pos=pos.filter(start_date__gte=datetime.datetime.today())
  if len(pos)==0:
    warn='आपकी आवश्यकता से मेल खाने वाला कोई परिणाम नहीं है|'
    return render(request,'worker/postresult.html',{'pos':pos,'warn':warn})
  loc=location.objects.get(username=request.user.username)
  for dat in pos :
    dis=discal(float(dat.lat),float(dat.lng),float(loc.lat),float(loc.lng))
    dat.distance=dis
    dat.save()
  pos=pos.order_by('distance')
  warn=""
  return render(request,'worker/postresult.html',{'pos':pos,'warn':warn})
