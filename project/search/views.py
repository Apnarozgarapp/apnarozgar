from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib.auth.models import User
from worker.models import Profile,location
from .models import Posts,Status
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
    address = request.POST.get('address',None)
    lat1 = request.POST.get('lat',None)
    lng1 = request.POST.get('lng',None)
    
    try :
      user1=Profile.objects.filter(Q(skill1=skill)|Q(skill2=skill)|Q(skill3=skill))    
      for data in user1:
        loc=location.objects.get(username=data.user.username)
        dis=discal(float(lat1),float(lng1),float(loc.lat),float(loc.lng))
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
    data= Profile.objects.get( user_id= dat)
    return render(request,'worker/view.html',{'data': data})  
  else:
    return HttpResponse(" No Worker available.") 

def work_post(request):
  if request.method == 'POST' and 'workdata' in request.POST:
      s_contact = request.POST.get('s_contact',None)
      rskill = request.POST.get('rskill',None)
      street = request.POST.get('street',None)
      locatio = request.POST.get('location',None)
      s_date = request.POST.get('start_date',None)
      e_date = request.POST.get('end_date',None)
      lat1 = request.POST.get('lat',None)
      lng1 = request.POST.get('lng',None)
      Nworker=request.POST.get('Nworker',None)
      Twork=request.POST.get('Twork',None)
      description=request.POST.get('description',None)
      status=request.POST.get('status',None)
      if lat1=='0':
        lat1='25.435801'
      if lng1=='0':
        lng1='81.846311'
      dat=Posts(username=request.user.username,name=request.user.first_name, s_contact=s_contact,rskill=rskill,street=street,start_date=s_date,Nworker=Nworker,Twork=Twork,location=locatio,end_date=e_date,lat=lat1,lng=lng1,description=description,status=status)
      dat.save()
      warn=""
      return render(request,'search/update.html',{'warn' : warn,'data':dat})
    

  else:
    return render(request,'search/pwork.html')

def see_work_post(request):
  if request.method=="POST" and 'delete' in request.POST:
    post_id=request.POST.get('post_id')
    data=Posts.objects.get(post_id=post_id)
    data.delete()
    data.save()
    pos=Posts.objects.filter(username=request.user.username)
    warn=""
    if len(pos)==0:
      warn="No posts found"
    return render(request,'search/postresult.html',{'pos':pos,'warn':warn})
  elif request.method=="POST" and 'status' in request.POST:
    post_id=request.POST.get('post_id')
    data=Posts.objects.get(post_id=post_id)
    if data.status=="public":
      data.status="private"
    else:
      data.status="public"
    data.save()
    warn=""
    return render(request,'search/update.html',{'data':data,'warn':warn})

  elif request.method=="POST" and 'selected' in request.POST:
    post_id=request.POST.get('post_id')
    data=Posts.objects.get(post_id=post_id)
    selected=Status.objects.filter(post_id=post_id)
    warn=""
    if len(selected)==0:
      warn="No  worker is selected"
    return render(request,'search/selected.html',{'data':data,'warn':warn,'selected':selected})

  elif request.method=="POST" and 'search' in request.POST:
    post_id=request.POST.get('post_id')
    sta=Status.objects.filter(post_id=post_id)
    data=Posts.objects.get(post_id=post_id)
    try :
        user1=Profile.objects.filter(Q(skill1=data.rskill)|Q(skill2=data.rskill)|Q(skill3=data.rskill))    
        user1 = user1.filter(start_date__lte=data.start_date,end_date__gte=data.end_date)
        if len(user1) == 0:
          warn = "आपकी आवश्यकता से मेल खाने वाला कोई परिणाम नहीं है|"
          return render(request,'search/update.html',{'data':data,'warn':warn})
        for dat in user1:
          loc= location.objects.get(username=dat.user.username)
          dis=discal(float(data.lat),float(data.lng),float(loc.lat),float(loc.lng))
          data.age=dis
          data.save()
        user1=user1.order_by('age')
        warn = " "
        return render(request,'search/presult.html',{'users' : user1, 'warn' : warn,'dat':data,'sta':sta})
    except Profile.DoesNotExist:
        warn="आपकी आवश्यकता से मेल खाने वाला कोई परिणाम नहीं है|"
        return render(request,'search/update.html',{'data':data,'warn':warn})

  elif request.method=="POST" and 'edit' in request.POST:
    post_id=request.POST.get('post_id')
    data=Posts.objects.get(post_id=post_id)
    return render(request,'search/pwork1.html',{'data':data})


  elif request.method=="POST" and 'gotopost' in request.POST:
    post_id=request.POST.get('post_id')
    data=Posts.objects.get(post_id=post_id)
    warn=""
    return render(request,'search/update.html',{'data':data,'warn':warn})

  elif request.method=="POST" and ('hire' in request.POST or 'chire' in request.POST ):
    post_id=request.POST.get('post_id')
    user_id=request.POST.get('user_id')
    worker=request.POST.get('worker')
    hirer=request.POST.get('hirer')
    abc=Status.objects.filter(post_id=post_id,user_id=user_id,worker=worker,hirer=hirer)
    if len(abc)==0 and 'hire' in request.POST:
      cba=Status(post_id=post_id,user_id=user_id,worker=worker,hirer=hirer,worker_status=user_id)
      cba.save()
    for dcba in abc:
      pqr=Status.objects.get(status_id=dcba.status_id)
      if 'chire' in request.POST:
        pqr.worker_status=""
      else:
        pqr.worker_status=user_id
      pqr.save()

    sta=Status.objects.filter(post_id=post_id)
    data=Posts.objects.get(post_id=post_id)
    try :
        user1=Profile.objects.filter(Q(skill1=data.rskill)|Q(skill2=data.rskill)|Q(skill3=data.rskill))    
        user1 = user1.filter(start_date__lte=data.start_date,end_date__gte=data.end_date)
        if len(user1) == 0:
          warn = "आपकी आवश्यकता से मेल खाने वाला कोई परिणाम नहीं है|"
          return render(request,'search/update.html',{'data':data,'warn':warn})
        for dat in user1:
          loc= location.objects.get(username=dat.user.username)
          dis=discal(float(data.lat),float(data.lng),float(loc.lat),float(loc.lng))
          data.age=dis
          data.save()
        user1=user1.order_by('age')
        warn = " "
        return render(request,'search/presult.html',{'users' : user1, 'warn' : warn,'dat':data,'sta':sta})
    except Profile.DoesNotExist:
        warn="आपकी आवश्यकता से मेल खाने वाला कोई परिणाम नहीं है|"
        return render(request,'search/update.html',{'data':data,'warn':warn})
  else:
    pos=Posts.objects.filter(username=request.user.username)
    warn=""
    if len(pos)==0:
      warn="No posts found"
    return render(request,'search/postresult.html',{'pos':pos,'warn':warn})

def update(request):
  if request.method=="POST" and 'update' in request.POST:
    post_id=request.POST.get('post_id',None)
    name=request.POST.get('name')
    s_contact = request.POST.get('s_contact',None)
    rskill = request.POST.get('rskill',None)
    street = request.POST.get('street',None)
    locatio = request.POST.get('location',None)
    s_date = request.POST.get('start_date',None)
    e_date = request.POST.get('end_date',None)
    lat1 = request.POST.get('lat',None)
    lng1 = request.POST.get('lng',None)
    Nworker=request.POST.get('Nworker',None)
    Twork=request.POST.get('Twork',None)
    description=request.POST.get('description',None)
    data=Posts.objects.get(post_id=post_id)
    data.name=name
    data.s_contact=s_contact
    data.rskill=rskill
    data.street==street
    data.location=locatio
    data.start_date=s_date
    data.end_date=e_date
    data.Nworker=Nworker
    data.Twork=Twork
    data.description=description
    if lat1 !='0':
      data.lat=lat1
      data.lng=lng1
    data.save()
    warn="submit successfully"
    return render(request,'search/update.html',{'data':data,'warn':warn})