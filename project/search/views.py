from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib.auth.models import User
from worker.models import Profile,location,Contractor,Current_location
from login.models import Feedback
from .models import Posts,Status
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django import forms
import re
import urllib.request
from math import sin, cos, sqrt, atan2, radians
from django.db.models import Q
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
@login_required
@transaction.atomic
def done(request):
	if request.user.username:
		if request.user.profile.loginas=="hirer":
			if request.method == 'POST' and 'done1' in request.POST:
				post_id=request.POST.get('post_id')
				user_id=request.POST.get('user_id')
				pmode=request.POST.get('pmode')
				pdate=request.POST.get('pdate')
				description=request.POST.get('description')
				rating=request.POST.get('rating')
				feedback1=request.POST.get('feedback1')
				feedback2=request.POST.get('feedback2')
				feedback3=request.POST.get('feedback3')
				page=request.POST.get('page')
				target=request.POST.get('target')
				wuser=Profile.objects.get(user_id=user_id)
				if not wuser.rating:
						wuser.rating=5
						wuser.nhirer=1

				wuser.rating=(wuser.rating*wuser.nhirer+float(rating))/(wuser.nhirer+1)
				wuser.nhirer=wuser.nhirer+1
				if feedback2!="नहीं आया":
					wuser.rating=wuser.rating*.80
				
					data1=Feedback(userhirer=request.user.username,target=target,userworker=wuser,post_id=post_id,feedback1=feedback1,feedback2=feedback2,feedback3=feedback3,pmode=pmode,pdate=pdate,description=description,done='a')
					data1.save()
				wuser.save()
				data=Posts.objects.get(post_id=post_id)
				data2=Status.objects.get(post_id=post_id,user_id=user_id)
				data2.done='a'
				data2.save()
				selected=Status.objects.filter(post_id=post_id,confirm='a')
				warn=" प्रतिक्रिया (Feedback) और भुगतान विवरण सफलतापूर्वक सबमिट किया गया "
				return render(request,"search/selected.html",{'data':data,'page':page,'selected':selected,'warn':warn})


			elif request.method == 'GET' and 'done' in request.GET:
				post_id=request.GET.get('post_id')
				user_id=request.GET.get('user_id')
				page=request.GET.get('page')
				data22=Status.objects.filter(post_id=post_id,user_id=user_id)
				if len(data22)==1:
					for data2 in data22:
						if data2.start_date<=datetime.datetime.today().date():
							return render(request,"search/done.html",{'post_id':post_id,'target':data2.target,'page':page,'user_id':user_id}) 
						else:
							data=Posts.objects.get(post_id=post_id)
							selected=Status.objects.filter(post_id=post_id,confirm='a')
							warn=" काम अभी तक शुरू नहीं हुआ है "
							return render(request,"search/selected.html",{'data':data,'page':page,'selected':selected,'warn':warn})
				else:
					pos=Posts.objects.filter(username=request.user.username)
					page=request.POST.get('page')
					warn=""
					if len(pos)==0:
						warn="कोई पोस्ट नहीं मिला।"
					if len(pos)!=0:
						pos=pos.order_by('-post_id')
					pag = Paginator(pos,4)
					if not page:
						page=1
					try:
						p = pag.page(int(page))
					except:
						p = pag.page(int(page))
					return render(request,'search/postresult.html',{'pos':p,'warn':warn})
			else:
				pos=Posts.objects.filter(username=request.user.username)
				if len(pos)!=0:
						pos=pos.order_by('-post_id')
				warn=""
				if len(pos)==0:
					warn="कोई पोस्ट नहीं मिला।"
				pag = Paginator(pos,4)
				page=request.POST.get('page')
				if not page:
					page=1
				p = pag.page(int(page))
				return render(request,'search/postresult.html',{'pos':p,'warn':warn})
		else:
			warn="कृपया पहले नियोक्ता के रूप में लॉगिन करें"
			return render(request,'login/form.html',{'warn':warn})
	else:
		warn="कृपया पहले  लॉगिन करें"
		return render(request,'login/form.html',{'warn':warn})


def search_result(request):
	if request.user.username:
		if request.user.profile.loginas=="hirer":
			if request.method == 'GET' and 'btn' in request.GET:
				target = request.GET.get('target',None)
				skill = request.GET.get('skill',None)
				address = request.GET.get('address',None)
				lat1 = request.GET.get('lat',None)
				lng1 = request.GET.get('lng',None)
				page = request.GET.get('page',None)
				if lat1=='0':
					lat1='25.435801'
					lng1='81.846311'
				try :
					if target=="a":
						user1=Profile.objects.filter(Q(skill1=skill)|Q(skill2=skill)|Q(skill3=skill))
					else:
						user1=Contractor.objects.filter(skill=skill)
					for data in user1:
						print(user1)
						loc=location.objects.get(username=data.user.username)
						dis=discal(float(lat1),float(lng1),float(loc.lat),float(loc.lng))
						data.dis=dis
						data.save()
					user1=user1.order_by('dis')
					warn = ""
					if len(user1) == 0:
						warn = "आपकी आवश्यकता से मेल खाने वाला कोई परिणाम नहीं है|"
					pag=Paginator(user1,10)
					try:
					 p = pag.page(int(page))
					except:
						p = pag.page(1)
					return render(request,'search/result.html',{'users' : p, 'warn' : warn,'address':address,'lat':lat1,'lng':lng1,'skill':skill,'target':target})
				except :
					warn = "आपकी आवश्यकता से मेल खाने वाला कोई परिणाम नहीं है|"
					return render(request,'search/search.html',{'warn':warn})  
			else:
				return render(request,'search/search.html')
		else:
			warn="कृपया पहले नियोक्ता के रूप में लॉगिन करें"
			return render(request,'login/form.html',{'warn':warn})
	else:
		warn="कृपया पहले  लॉगिन करें"
		return render(request,'login/form.html',{'warn':warn})


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
  return round(distance,4)


def view_worker(request):
	if request.user.username:
		dat = request.GET['data']
		target=request.GET['target']
		try:
			if target =='a':
				data= Profile.objects.get(user_id = dat)
				current_address2=Current_location.objects.filter(username=data)
				if len(current_address2)==1:
					for current_address1 in current_address2:
						return render(request,'worker/view.html',{'data':data,'current_address':current_address1})	

				else:
					return render(request,'worker/view.html',{'data':data})
			elif target =='b':
				data= Profile.objects.get(user_id = dat)
				current_address2=Current_location.objects.filter(username=data)
				skilllist=Contractor.objects.filter(user=data.user)
				if len(current_address2)==1:
					for current_address1 in current_address2:
						return render(request,'worker/hcview.html',{'data':data,'current_address':current_address1,'skilllist':skilllist})
				else:
					return render(request,'worker/hcview.html',{'data':data,'skilllist':skilllist})
			else:
				warn="कोई मजदूर/ठेकेदार नहीं है"
				return render(request,'worker/view.html',{'warn': warn})
		except:
			warn="कोई मजदूर/ठेकेदार नहीं है"
			return render(request,'worker/view.html',{'warn': warn})
	else:
		warn="कृपया पहले  लॉगिन करें"
		return render(request,'login/form.html',{'warn':warn})



def work_post(request):
	if request.user.username:
		if request.user.profile.loginas=="hirer":
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
				Twork=request.POST.getlist('Twork',None)
				description=request.POST.get('description',None)
				status=request.POST.get('status',None)
				target=request.POST.get('target',None)
				if lat1=='0':
					lat1='25.435801'
					lng1='81.846311'
				try:
					dat=Posts(target=target,username=request.user.username,name=request.user.first_name, s_contact=s_contact,rskill=rskill,street=street,start_date=s_date,Nworker=Nworker,Twork=Twork,location=locatio,end_date=e_date,lat=lat1,lng=lng1,description=description,status=status)
					dat.save()
					dataa=Posts.objects.get(post_id=dat.post_id)
					if target=='a':
						warn="कार्यकर्ता के लिए आपकी पोस्ट"
					else:
						warn="ठेकेदार के लिए आपकी पोस्ट"
					page=1
					return render(request,'search/update.html',{'warn' : warn,'page':page,'data':dataa})
				except:
					warn="कृपया पुन: प्रयास करें"
					return render(request,'search/pwork.html',{'warn':warn})
			else:
				return render(request,'search/pwork.html')
		else:
			warn="कृपया पहले नियोक्ता के रूप में लॉगिन करें"
			return render(request,'login/form.html',{'warn':warn})
	else:
		warn="कृपया पहले  लॉगिन करें"
		return render(request,'login/form.html',{'warn':warn})


def see_work_post(request):
 if request.user.username:
  if request.user.profile.loginas=="hirer":
   if request.method=="GET" and 'delete' in request.GET:
    post_id=request.GET.get('post_id')
    page=request.GET.get('page')
    data=Posts.objects.filter(post_id=post_id,username=request.user.username)

    warn=""
    if len(data)==1:
      for dataa in data:
        data3=Status.objects.filter(post_id=dataa.post_id,confirm='a')
        if len(data3)>0:
          warn="आप काम को नहीं हटा सकते क्योंकि कुछ श्रमिक चयनित है। अगर आप हटाना चाहते हैं, तो पहले श्रमिक को अचयनित करें "
        else:
          dataa.delete()
          warn = "एक पोस्ट को हटा दिया गया है"
    else:
       warn="कार्य आईडी सही नहीं है, या आप सही उपयोगकर्ता नहीं हैं"
    pos=Posts.objects.filter(username=request.user.username)
    if len(pos)!=0:
      pos=pos.order_by('-post_id')
    if len(pos)==0:
      warn="कोई पोस्ट नहीं मिला।"
    pag = Paginator(pos,4)
    if pag.num_pages < int(page):
           page=int(page)-1
    if not page:
              page='1'
    try:
       p = pag.page(int(page))
    except:
       p = pag.page(1)
    return render(request,'search/postresult.html',{'pos':p,'warn':warn})


   elif request.method=="GET" and 'status' in request.GET:
    post_id=request.GET.get('post_id')
    page=request.GET.get('page')
    data=Posts.objects.filter(post_id=post_id,username=request.user.username)
    warn=""
    if len(data)==1:
      for dataa in data:
        if dataa.status=="public":
          dataa.status="private"
        else:
          dataa.status="public"
        dataa.save()
    else:
      warn="पोस्ट आईडी सही नहीं है, या आप सही उपयोगकर्ता नहीं हैं"
    pos=Posts.objects.filter(username=request.user.username)
    if len(pos)!=0:
      pos=pos.order_by('-post_id')
    pag = Paginator(pos,4)

    if not page:
              page='1'
    try:
        p = pag.page(int(page))
    except:
        p=pag.page(1)
    return render(request,'search/postresult.html',{'pos':p,'warn':warn})


   elif request.method=="GET" and 'selected' in request.GET:
    post_id=request.GET.get('post_id')
    page=request.GET.get('page')
    data=Posts.objects.filter(post_id=post_id,username=request.user.username)
    if len(data)==1:
      selected=Status.objects.filter(post_id=post_id,confirm='a')
      warn=""
      if len(selected)==0:
        warn="कोई भी श्रमिक चयनित नहीं है"
      for dataa in data:
       return render(request,'search/selected.html',{'page':page,'data':dataa,'warn':warn,'selected':selected})
    else:
      warn="पोस्ट आईडी सही नहीं है, या आप सही उपयोगकर्ता नहीं हैं"
      pos=Posts.objects.filter(username=request.user.username)
      if len(pos)!=0:
        pos=pos.order_by('-post_id')
      pag = Paginator(pos,4)
      if not page:
              page='1'
      try:
        p = pag.page(int(page))
      except:
        p = pag.page(1)
      return render(request,'search/postresult.html',{'pos':p,'warn':warn})  


   elif request.method=="GET" and 'search' in request.GET:
    post_id=request.GET.get('post_id')
    page=request.GET.get('page')
    dataa=Posts.objects.filter(post_id=post_id,username=request.user.username)
    if len(dataa)==1:
        for data in dataa:
          sta=Status.objects.filter(post_id=post_id,target=data.target)
          try :
            if data.target=='a':
                user1=Profile.objects.filter(Q(skill1=data.rskill)|Q(skill2=data.rskill)|Q(skill3=data.rskill))    
                user1 = user1.filter(start_date__lte=data.start_date,end_date__gte=data.end_date)
            elif data.target=='b':
                user1=Contractor.objects.filter(skill=data.rskill,start_date__lte=data.start_date,end_date__gte=data.end_date)
            if len(user1) == 0:
              warn = "आपकी आवश्यकता से मेल खाने वाला कोई परिणाम नहीं है|"
              pos=Posts.objects.filter(username=request.user.username)
              if len(pos)!=0:
                 pos=pos.order_by('-post_id')
              pag = Paginator(pos,4)
              p = ""
              if not page:
                page='1'
                p = pag.page(int(page))
              return render(request,'search/postresult.html',{'pos':p,'warn':warn})
            for dat in user1:
              r=Status.objects.filter(user_id=dat.user_id,confirm='a',target=data.target)
              p=r.filter(Q(start_date__lte=data.start_date,end_date__gte=data.start_date)|Q(start_date__lte=data.end_date,end_date__gte=data.end_date)|Q(start_date__lte=data.start_date,end_date__gte=data.end_date)|Q(start_date__gte=data.start_date,end_date__lte=data.end_date))
              loc= location.objects.get(username=dat.user.username)
              dis=discal(float(data.lat),float(data.lng),float(loc.lat),float(loc.lng))
              dat.dis=dis
              if len(p)!=0:
                dat.joinrequest='e'
                for pp in p:
                  if pp.post_id==data.post_id:
                   
                      dat.joinrequest='a'
                    
              else:
                f=sta.filter(user_id=dat.user_id)
                if len(f)==0:
                  dat.joinrequest='d'
                else:
                  for ff in f:    
                    if ff.user_id==ff.hirer_status and ff.post_id ==ff.worker_status:
                      dat.joinrequest='a'
                    elif ff.user_id==ff.hirer_status:
                      dat.joinrequest='b'
                    elif ff.post_id ==ff.worker_status:
                      dat.joinrequest='c'
                    
              dat.save()
            user1=user1.order_by('dis')
            warn = " "
            pag = Paginator(user1,6)
            rpage = request.GET.get('rpage',None)
            if not rpage:
              rpage='1'
            p = pag.page(int(rpage))
            return render(request,'search/presult.html',{'users' : p,'page':page ,'warn' : warn,'dat':data})
          except Profile.DoesNotExist:
            warn="आपकी आवश्यकता से मेल खाने वाला कोई परिणाम नहीं है|"
            pos=Posts.objects.filter(username=request.user.username)
            if len(pos)!=0:
               pos=pos.order_by('-post_id')
            pag = Paginator(pos,4)
            if not page:
              page='1'
            try:
                p = pag.page(int(page))
            except:
                p = pag.page(1)
            return render(request,'search/postresult.html',{'pos':p,'warn':warn})
    else:
      warn="पोस्ट आईडी सही नहीं है, या आप सही उपयोगकर्ता नहीं हैं"
      pos=Posts.objects.filter(username=request.user.username)
      if len(pos)!=0:
        pos=pos.order_by('-post_id')
      pag = Paginator(pos,4)
      if not page:
              page='1'
      try:
        p = pag.page(int(page))
      except:
        p = pag.page(1)
      return render(request,'search/postresult.html',{'pos':p,'warn':warn})


   elif request.method=="GET" and 'edit' in request.GET:
    post_id=request.GET.get('post_id')
    page = request.GET.get('page',None)
    dataa=Posts.objects.filter(post_id=post_id,username=request.user.username)
    if len(dataa)==1:
      for data in dataa:
          data3=Status.objects.filter(post_id=data.post_id,confirm='a')
          if len(data3)>0:
            warn="आप काम को नहीं बदल सकते क्योंकि कुछ श्रमिक चयनित होता है। अगर आप बदलना चाहते हैं, तो पहले श्रमिक को अचयनित करें "
          else:
            return render(request,'search/pwork1.html',{'page':page,'data':data})
    else:
      warn="पोस्ट आईडी सही नहीं है, या आप सही उपयोगकर्ता नहीं हैं"
    pos=Posts.objects.filter(username=request.user.username)
    if len(pos)!=0:
      pos=pos.order_by('-post_id')
    pag = Paginator(pos,4)
    if not page:
            page='1'
    try:
        p = pag.page(int(page))
    except:
        p = pag.page(1)
    return render(request,'search/postresult.html',{'pos':p,'warn':warn})


   elif request.method=="GET" and 'gotopost' in request.GET:
    post_id=request.GET.get('post_id')
    page = request.GET.get('page',None)
    dataa=Posts.objects.filter(post_id=post_id,username=request.user.username)
    if len(dataa)==1:
     for data in dataa:
      return render(request,'search/update.html',{'data':data,'page':page})
    else:
      warn="पोस्ट आईडी सही नहीं है, या आप सही उपयोगकर्ता नहीं हैं"
      pos=Posts.objects.filter(username=request.user.username)
      if len(pos)!=0:
        pos=pos.order_by('-post_id')
      pag = Paginator(pos,4)
      if not page:
              page='1'
      p = pag.page(int(page))
      return render(request,'search/postresult.html',{'pos':p,'warn':warn})

   elif request.method=="POST" and ('hire' in request.POST or 'chire' in request.POST ):
    post_id=request.POST.get('post_id')
    user_id=request.POST.get('user_id')
    worker=request.POST.get('worker')
    hirer=request.POST.get('hirer')
    userworker=request.POST.get('userworker')
    userhirer=request.POST.get('userhirer')
    start_date=request.POST.get('start_date')
    end_date=request.POST.get('end_date')
    page = request.POST.get('page',None)
    rpage = request.POST.get('rpage',None)
    target=request.POST.get('target',None)
    dataa=Posts.objects.filter(post_id=post_id,username=request.user.username)
    if len(dataa)==1:
      abc=Status.objects.filter(post_id=post_id,user_id=user_id)
      rr=Status.objects.filter(user_id=user_id,confirm='a',target=target)
      pp=rr.filter(Q(start_date__lte=start_date,end_date__gte=start_date)|Q(start_date__lte=end_date,end_date__gte=end_date)|Q(start_date__lte=start_date,end_date__gte=end_date)|Q(start_date__gte=start_date,end_date__lte=end_date))
      if len(pp)==0:
        if len(abc)==0 and 'hire' in request.POST:
          cba=Status(target=target, post_id=post_id,user_id=user_id,worker=worker,hirer=hirer,hirer_status=user_id,userworker=userworker,userhirer=userhirer,start_date=start_date,end_date=end_date)
          cba.save()
        else:
          for pqr in abc:
            if 'hire' in request.POST:
              pqr.hirer_status=user_id
              pqr.confirm='a'
              pqr.save()
          if 'chire' in request.POST:
            if pqr.confirm !='a':
              pqr.delete()
            else:
              pqr.hirer_status=0
              pqr.save()

      sta=Status.objects.filter(post_id=post_id)
      data=Posts.objects.get(post_id=post_id)
      try :
        if data.target=='a':
            user1=Profile.objects.filter(Q(skill1=data.rskill)|Q(skill2=data.rskill)|Q(skill3=data.rskill))    
            user1 = user1.filter(start_date__lte=data.start_date,end_date__gte=data.end_date)
        elif data.target=='b':
            user1 = Contractor.objects.filter(skill=data.rskill,start_date__lte=data.start_date,end_date__gte=data.end_date)
        if len(user1) == 0:
          warn = "आपकी आवश्यकता से मेल खाने वाला कोई परिणाम नहीं है|"
          return render(request,'search/update.html',{'data':data,'warn':warn})
        for dat in user1:
          r=Status.objects.filter(user_id=dat.user_id,confirm='a',target=data.target)
          p=r.filter(Q(start_date__lte=data.start_date,end_date__gte=data.start_date)|Q(start_date__lte=data.end_date,end_date__gte=data.end_date)|Q(start_date__lte=data.start_date,end_date__gte=data.end_date)|Q(start_date__gte=data.start_date,end_date__lte=data.end_date))
          loc= location.objects.get(username=dat.user.username)
          dis=discal(float(data.lat),float(data.lng),float(loc.lat),float(loc.lng))
          dat.dis=dis
          if len(p)!=0:
            dat.joinrequest='e'
            for pp in p:
              if pp.post_id==data.post_id:
                  dat.joinrequest='a'
               
          else:
            f=sta.filter(user_id=dat.user_id)
            if len(f)==0:
              dat.joinrequest='d'
            else:
              for ff in f:    
                if ff.user_id==ff.hirer_status and ff.post_id ==ff.worker_status:
                    dat.joinrequest='a'
                elif ff.user_id==ff.hirer_status:
                  dat.joinrequest='b'
                elif ff.post_id ==ff.worker_status:
                  dat.joinrequest='c'
                
          dat.save()
        user1=user1.order_by('dis')
        warn = " "
        pag = Paginator(user1,6)
        if not rpage:
          rpage='1'
        p = pag.page(int(rpage))
        return render(request,'search/presult.html',{'users' : p,'page':page, 'warn' : warn,'dat':data})
      except Profile.DoesNotExist:
        warn="आपकी आवश्यकता से मेल खाने वाला कोई परिणाम नहीं है|"
        return render(request,'search/update.html',{'data':data,'page':page,'warn':warn})
    else:
      warn="पोस्ट आईडी सही नहीं है, या आप सही उपयोगकर्ता नहीं हैं"
      pos=Posts.objects.filter(username=request.user.username)
      if len(pos)!=0:
        pos=pos.order_by('-post_id')
      pag = Paginator(pos,4)
      if not page:
              page='1'
      try:
        p = pag.page(int(page))
      except:
        p = pag.page(1)
      return render(request,'search/postresult.html',{'pos':p,'warn':warn})


   elif request.method=="POST" and ('schire' in request.POST or 'shire' in request.POST):
    post_id=request.POST.get('post_id')
    user_id=request.POST.get('user_id')
    page=request.POST.get('page')
    dataa=Posts.objects.filter(post_id=post_id,username=request.user.username)
    if len(dataa)==1:
      pqr=Status.objects.filter(post_id=post_id,user_id=user_id)
      if len(pqr)==1:
        for pq in pqr:
          if 'shire' in request.POST:
            pq.hirer_status=user_id
            pq.save()
          elif 'schire' in request.POST and pq.worker_status!=pq.post_id:
            pq.delete()
          elif 'schire' in request.POST and pq.worker_status== pq.post_id:
            pq.hirer_status=0
            pq.save()
      for data in dataa:
        selected=Status.objects.filter(post_id=post_id,confirm='a')
        warn=""
        if len(selected)==0:
          warn="कोई भी श्रमिक चयनित नहीं है"
        return render(request,'search/selected.html',{'data':data,'page':page,'warn':warn,'selected':selected})
    else:
      warn="पोस्ट आईडी सही नहीं है, या आप सही उपयोगकर्ता नहीं हैं"
      pos=Posts.objects.filter(username=request.user.username)
      if len(pos)!=0:
        pos=pos.order_by('-post_id')
      pag = Paginator(pos,4)
      if not page:
              page='1'
      p = pag.page(int(page))
      return render(request,'search/postresult.html',{'pos':p,'warn':warn})

   else:
    pos=Posts.objects.filter(username=request.user.username)
    if len(pos)!=0:
        pos=pos.order_by('-post_id')
    warn=""
    if len(pos)==0:
      warn="कोई पोस्ट नहीं मिला।"
    pag = Paginator(pos,4)
    page = request.GET.get('page',None)
    if not page:
      page='1'
    p = pag.page(int(page))
    return render(request,'search/postresult.html',{'pos':p,'warn':warn})
  else:
    warn="कृपया पहले नियोक्ता के रूप में लॉगिन करें"
    return render(request,'login/form.html',{'warn':warn})
 else:
   warn="कृपया पहले  लॉगिन करें"
   return render(request,'login/form.html',{'warn':warn})

def update(request):
 if request.user.username:
  if request.user.profile.loginas=="hirer":
   if request.method=="POST" and 'update' in request.POST:
    post_id=request.POST.get('post_id',None)
    name=request.POST.get('name')
    s_contact = request.POST.get('s_contact',None)
    street = request.POST.get('street',None)
    locatio = request.POST.get('location',None)
    lat1 = request.POST.get('lat',None)
    lng1 = request.POST.get('lng',None)
    Nworker=request.POST.get('Nworker',None)
    Twork=request.POST.getlist('Twork',None)
    description=request.POST.get('description',None)
    page = request.POST.get('page',None)
    dataa=Posts.objects.filter(post_id=post_id,username=request.user.username)
    if len(dataa)==1:
     for data in dataa:
      data.name=name
      data.s_contact=s_contact
      data.street==street
      data.location=locatio
      data.Nworker=Nworker
      data.Twork=Twork
      data.description=description
      data.lat=lat1
      data.lng=lng1
      data.save()
      data1=Posts.objects.get(post_id=post_id)
      warn="डेटा को सफलतापूर्वक सबमिट किया गया है"
      return render(request,'search/update.html',{'data':data1,'page':page,'warn':warn})
    else:
      warn="पोस्ट आईडी सही नहीं है, या आप सही उपयोगकर्ता नहीं हैं"
      pos=Posts.objects.filter(username=request.user.username)
      if len(pos)!=0:
        pos=pos.order_by('-post_id')
      pag = Paginator(pos,4)
      if not page:
              page='1'
      try:
        p = pag.page(int(page))
      except:
        p = pag.page(1)
      return render(request,'search/postresult.html',{'pos':p,'warn':warn})

   else:
    pos=Posts.objects.filter(username=request.user.username)
    if len(pos)!=0:
        pos=pos.order_by('-post_id')
    warn=""
    if len(pos)==0:
      warn="कोई पोस्ट नहीं मिला।"
    pag = Paginator(pos,4)
    if not page:
              page='1'
    try:
        p = pag.page(int(page))
    except:
        p = pag.page(1)
    return render(request,'search/postresult.html',{'pos':pos,'warn':warn})
  else:
    warn="कृपया पहले नियोक्ता के रूप में लॉगिन करें"
    return render(request,'login/form.html',{'warn':warn})
 else:
   warn="कृपया पहले  लॉगिन करें"
   return render(request,'login/form.html',{'warn':warn})