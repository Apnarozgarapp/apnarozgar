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
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
@login_required
@transaction.atomic


def confirm_work(request):
  if request.method=="POST" and 'cwchire' in request.POST:
    post_id=request.POST.get('post_id')
    user_id=request.POST.get('user_id')
    page=request.POST.get('page')
    pq=Status.objects.filter(post_id=post_id,user_id=user_id)
    if len(pq)!=0:
       for pqr in pq:
          pqr.delete()
    selected=Status.objects.filter(userworker=request.user.username,confirm='a')
    warn=""
    if len(selected)==0:
      warn="आप किसी भी पोस्ट के लिए अभी तक चयनित नहीं हैं।"
    pag = Paginator(selected,3)
    p = pag.page(int(page))
    return render(request,'worker/confirm_work.html',{'warn':warn,'selected':p})
  else:
    selected=Status.objects.filter(userworker=request.user.username,confirm='a')
    warn=""
    if len(selected)==0:
      warn="आप किसी भी पोस्ट के लिए अभी तक चयनित नहीं हैं।"
    pag = Paginator(selected,3)
    page = request.GET.get('page',None)
    if not page:
      page='1'
    p = pag.page(int(page))
    return render(request,'worker/confirm_work.html',{'warn':warn,'selected':p})

def detail_post(request):
  if request.method == 'GET':
    dat = request.GET['data']
    data= Posts.objects.filter( post_id= dat)
    if len(data)!=0:
    	for data1 in data:
    		return render(request,'search/view.html',{'data': data1})
    else:
    	warn="कोई पोस्ट नहीं मिला"  
    	return render(request,'search/view.html',{'warn': warn})
  else:
    return HttpResponse("कोई पोस्ट नहीं मिला।") 

def update_profile(request):
  
    if request.method == 'POST' and 'save_changes1' in request.POST:
        profile_form = ProfileForm1(request.POST, instance=request.user.profile)
        lat=request.POST.get('lat')
        lng=request.POST.get('lng')
        name=request.POST.get('first_name')
        request.user.first_name=name
        request.user.save()
        if profile_form.is_valid():
            profile_form.save()
            if lat != '0':
                da=location(username=request.user.username,lat=lat,lng=lng)
                da.save()
            else:
                da=location.objects.filter(username=request.user.username)
                if len(da)==0:
                    da=location(username=request.user.username,lat='25.435801',lng='81.846311')
                    da.save()
            return render(request,'worker/worker2.html')
        else:
          warn ="कृपया विवरण को सही करें"
          return render(request,'worker/worker1.html',{"warn":warn})
    if request.method == 'POST' and 'save_changes2' in request.POST:
      skill1 = request.POST.get('skill1')
      warn = ""
      profile_form = ProfileForm2(request.POST, instance=request.user.profile)
      if profile_form.is_valid() and skill1:
         profile_form.save()
         return render(request,'worker/success.html',{"warn":warn})
      else:
          warn ="कृपया विवरण को सही करें, कौशल 1 अनिवार्य है।"
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
  pos=pos.filter(end_date__gte=datetime.datetime.today().date())

  if len(pos)==0:
    warn='आपकी आवश्यकता से मेल खाने वाला कोई परिणाम नहीं है|'
    return render(request,'worker/postresult.html',{'pos':pos,'warn':warn})
  loc=location.objects.get(username=request.user.username)
  for dat in pos :
    dis=discal(float(dat.lat),float(dat.lng),float(loc.lat),float(loc.lng))
    dat.distance=dis
    dat.save()
  pos=pos.order_by('distance')
  pag = Paginator(pos,2)
  page = request.GET.get('page',None)
  if not page:
    page='1'
  p = pag.page(int(page))
  warn=""
  return render(request,'worker/allpostresult.html',{'pos':p,'warn':warn})

def viewpost(request):
  if request.method=="POST" and ('whire' in request.POST or 'wchire' in request.POST ):
    post_id=request.POST.get('post_id')
    user_id=request.POST.get('user_id')
    worker=request.POST.get('worker')
    hirer=request.POST.get('hirer')
    userworker=request.POST.get('userworker')
    userhirer=request.POST.get('userhirer')
    start_date=request.POST.get('start_date')
    end_date=request.POST.get('end_date')
    page=request.POST.get('page')
    abc=Status.objects.filter(post_id=post_id,user_id=user_id)
    if len(abc)==0 and 'whire' in request.POST:
      cba=Status(post_id=post_id,user_id=user_id,worker=worker,hirer=hirer,worker_status=post_id,userworker=userworker,userhirer=userhirer,start_date=start_date,end_date=end_date)
      cba.save()
    else:
      pqr=Status.objects.get(post_id=post_id,user_id=user_id)
      pqr.worker_status=post_id
      pqr.confirm='a'
      pqr.save()
      if 'wchire' in request.POST:
        pqr.delete()
    sta=Status.objects.filter(user_id=user_id)
    data=Profile.objects.get(user=request.user)
    pos=Posts.objects.filter(Q(rskill=data.skill1)|Q(rskill=data.skill2)|Q(rskill=data.skill3))
    pos=pos.filter(status='public')
    pos=pos.filter(end_date__gte=datetime.datetime.today().date())
    if len(pos)==0:
      warn='आपकी आवश्यकता से मेल खाने वाला कोई परिणाम नहीं है|'
      return render(request,'worker/postresult.html',{'pos':pos,'warn':warn})
    loc=location.objects.get(username=request.user.username)
    for dat in pos :
      r=Status.objects.filter(user_id=data.user_id,confirm='a')
      p=r.filter(Q(start_date__lte=dat.start_date,end_date__gte=dat.start_date)|Q(start_date__lte=dat.end_date,end_date__gte=dat.end_date)|Q(start_date__lte=dat.start_date,end_date__gte=dat.end_date)|Q(start_date__gte=dat.start_date,end_date__lte=dat.end_date))
      dis=discal(float(dat.lat),float(dat.lng),float(loc.lat),float(loc.lng))
      dat.distance=dis
      if len(p)!=0:
        dat.temp='e'
        for pp in p:
              if pp.post_id==dat.post_id:
                dat.temp='a'
      else:
        f=sta.filter(post_id=dat.post_id)
        if len(f)==0:
          dat.temp='d'
        else:
          for ff in f:
            if ff.post_id==ff.worker_status and ff.user_id==ff.hirer_status:
                  dat.temp='a'
            elif ff.post_id==ff.worker_status:
                  dat.temp='b'
            elif ff.user_id==ff.hirer_status:
                  dat.temp='c' 
      dat.save()
    pos=pos.order_by('distance')
    warn=""
    pag = Paginator(pos,2)  
    p = pag.page(int(page))
    return render(request,'worker/postresult.html',{'pos':p,'user1':data,'warn':warn})
  else:

    data=Profile.objects.get(user=request.user)
    
    pos=Posts.objects.filter(Q(rskill=data.skill1)|Q(rskill=data.skill2)|Q(rskill=data.skill3))
    pos=pos.filter(status='public')
    pos=pos.filter(end_date__gte=datetime.datetime.today().date())
    if len(pos)==0:
      warn='आपकी आवश्यकता से मेल खाने वाला कोई परिणाम नहीं है|'
      return render(request,'worker/postresult.html',{'pos':pos,'warn':warn})
    loc=location.objects.get(username=request.user.username)
    sta=Status.objects.filter(user_id=data.user_id)
    for dat in pos :
      r=Status.objects.filter(user_id=data.user_id,confirm='a')
      p=r.filter(Q(start_date__lte=dat.start_date,end_date__gte=dat.start_date)|Q(start_date__lte=dat.end_date,end_date__gte=dat.end_date)|Q(start_date__lte=dat.start_date,end_date__gte=dat.end_date)|Q(start_date__gte=dat.start_date,end_date__lte=dat.end_date))  
      dis=discal(float(dat.lat),float(dat.lng),float(loc.lat),float(loc.lng))
      dat.distance=dis
      if len(p)!=0:
        dat.temp='e'
        for pp in p:
              if pp.post_id==dat.post_id:
                dat.temp='a'
      else:
        f=sta.filter(post_id=dat.post_id)
        if len(f)==0:
          dat.temp='d'
        else:
          for ff in f:
            if ff.post_id==ff.worker_status and ff.user_id==ff.hirer_status:
                  dat.temp='a'
            elif ff.post_id==ff.worker_status:
                  dat.temp='b'
            elif ff.user_id==ff.hirer_status:
                  dat.temp='c' 
      dat.save()
    pos=pos.order_by('distance')
    pag = Paginator(pos,2)
    page = request.GET.get('page',None)
    if not page:
      page='1'
    p = pag.page(int(page))
    warn=""
    return render(request,'worker/postresult.html',{'pos':p,'user1':data,'warn':warn})
