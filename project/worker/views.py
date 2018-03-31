from django.shortcuts import render
from .forms import  ProfileForm1,ProfileForm2
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib.auth.models import User
from .models import Profile,location
from search.models import Posts,Status
import login
import re
import urllib.request
from django.db.models import Q
from math import sin, cos, sqrt, atan2, radians
import datetime
@login_required
@transaction.atomic

def detail_post(request):
  if request.method == 'GET':
    dat = request.GET['data']
    data= Posts.objects.get( post_id= dat)
    return render(request,'search/view.html',{'data': data})  
  else:
    return HttpResponse(" No post available.") 

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

def all_post(request):
  pos=Posts.objects.filter(status='public')
  pos=pos.filter(start_date__gte=datetime.datetime.today())
  if len(pos)==0:
    warn=' No post is available|'
    return render(request,'worker/postresult.html',{'pos':pos,'warn':warn})
  loc=location.objects.get(username=request.user.username)
  for dat in pos :
    dis=discal(float(dat.lat),float(dat.lng),float(loc.lat),float(loc.lng))
    dat.distance=dis
    dat.save()
  pos=pos.order_by('distance')
  warn=""
  return render(request,'worker/allpostresult.html',{'pos':pos,'warn':warn})

def viewpost(request):
  if request.method=="POST" and ('whire' in request.POST or 'wchire' in request.POST ):
    post_id=request.POST.get('post_id')
    user_id=request.POST.get('user_id')
    worker=request.POST.get('worker')
    hirer=request.POST.get('hirer')
    userworker=request.POST.get('userworker')
    userhirer=request.POST.get('userhirer')
    abc=Status.objects.filter(post_id=post_id,user_id=user_id)
    if len(abc)==0 and 'whire' in request.POST:
      cba=Status(post_id=post_id,user_id=user_id,worker=worker,hirer=hirer,worker_status=post_id,userworker=userworker,userhirer=userhirer)
      cba.save()
    pqr=Status.objects.get(post_id=post_id,user_id=user_id)
    if 'wchire' in request.POST :
      pqr.worker_status=0
    else:
      pqr.worker_status=post_id
    pqr.save()
    if 'wchire' in request.POST and pqr.hirer_status!= user_id:
      pqr.delete()
    sta=Status.objects.filter(user_id=user_id)
    sta1=" "
    sta2=" "
    for pqrs in sta:
      sta1=sta1+str(pqrs.hirer_status)
      sta2=sta2+str(pqrs.worker_status)
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
      if str(dat.post_id) in sta2 and str(data.user_id) in sta1 :
            dat.temp='a'
      elif str(dat.post_id) in sta2:
            dat.temp='b'
      elif str(data.user_id) in sta1:
            dat.temp='c'
      else:
            dat.temp='d' 
      dat.save()
    pos=pos.order_by('distance')
    warn=""
    return render(request,'worker/postresult.html',{'pos':pos,'user1':data,'warn':warn})
  else:

    data=Profile.objects.get(user=request.user)
    sta=Status.objects.filter(user_id=data.user_id)
    sta1=" "
    sta2=" "
    for pqrs in sta:
      sta1=sta1+str(pqrs.hirer_status)
      sta2=sta2+str(pqrs.worker_status)
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
      if str(dat.post_id) in sta2 and str(data.user_id) in sta1 :
            dat.temp='a'
      elif str(dat.post_id) in sta2:
            dat.temp='b'
      elif str(data.user_id) in sta1:
            dat.temp='c'
      else:
            dat.temp='d' 
      dat.save()
    pos=pos.order_by('distance')
    warn=""
    return render(request,'worker/postresult.html',{'pos':pos,'user1':data,'warn':warn})
