from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)
from django.contrib.auth.models import User
import random
from .forms import UserLoginForm, UserRegisterForm
from .models import Registration_otp
from search.models import Status
from worker.models import Current_location
from django.core.mail import EmailMessage
import re
import string
from django.db.models import Q
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import urllib.request
import urllib.parse
import os
from .way2sms import sms,futuresms

#print(datetime.datetime.utcnow().strftime("%A, %d. %B %Y %I:%M%p"))
def query(request):
	if request.user.username:
		if request.method=="POST":
			username=request.POST.get('username')
			name=request.POST.get('name')
			problem=request.POST.get('problem')
			email=EmailMessage('Problem from Apna Rozgar user:-  '+name +'('+username+')', problem, to=['ramnarayanjamon@gmail.com'])
			email.send()
			warn="आपकी तकनीकी समस्या सफलतापूर्वक हमारे डेवलपर टीम को भेजी गई"
			return render(request,'login/aboutus.html',{'warn':warn})
		else:
			return render(request,'login/query.html')

	else:
		warn="कृपया पहले  लॉगिन करें"
		return render(request,'login/form.html',{'warn':warn})

def sendSMS(apikey, numbers, sender, message):
	params = {'apikey': apikey, 'numbers': numbers, 'message' : message, 'sender': sender}
	f = urllib.request.urlopen('https://api.textlocal.in/send/?'+ urllib.parse.urlencode(params))
	return (f.read(), f.code)

def smss(request):
	#futuresms(phno=phno,passwd=password,set_time='17:47',set_date='15/12/2017',receivernum=receiver mobile num,message='helloworld!!')
	sms(phno='8601867011',passwd='Ram2003',message='hey',receivernum='9005285986')
	return render(request,'login/form.html')

def aboutus(request):
	return render(request,'login/aboutus.html')

def Developer(request):
	return render(request,'login/developer.html')

def change_role(request):
	if request.user.username:
		if request.method=="POST":
			loginas1=request.POST.get('loginas')
			request.user.profile.loginas=loginas1
			request.user.profile.save()
			if loginas1=="worker" :
				return render(request,'worker/viewedit.html')
			elif loginas1=="contractor":
				return render(request,'worker/profilecontractor.html')
			elif loginas1=="hirer":
				return render(request,'search/hirer.html')
			else:
				return render(request,'login/form.html',{"form":form})
		else:
			if request.user.profile.loginas=="worker":        
				return render(request,'worker/viewedit.html')
			elif  request.user.profile.loginas=="contractor":
				return render(request,'worker/profilecontractor.html')
			elif request.user.profile.loginas=="hirer":
				return render(request,'search/hirer.html')
			else:
				warn="कृपया पहले  लॉगिन करें"
				return render(request,'login/form.html',{'warn':warn})
	else:
		warn="कृपया पहले  लॉगिन करें"
		return render(request,'login/form.html',{'warn':warn})	
def login_view(request):
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		loginas1 = form.cleaned_data.get("loginas")
		user = authenticate(username = username, password = password)
		if not user or not user.check_password(password) or not user.is_active:
			warn="उपयोगकर्ता नाम/ पासवर्ड गलत है । कृपया पुन: प्रयास करें|(Wrong username or password)"
			return render(request,'login/form.html',{"form":form,"warn":warn})
		login(request,user)
		request.user.is_authenticated()
		request.user.profile.loginas=loginas1
		request.user.profile.save()
		if loginas1=="worker" :
			return render(request,'worker/viewedit.html')
		elif loginas1=="contractor":
			return render(request,'worker/profilecontractor.html')
		elif loginas1=="hirer":
			return render(request,'search/hirer.html')
		else:
			return render(request,'login/form.html',{"form":form})
	elif request.user.username:

		if request.user.profile.loginas=="worker":        
			return render(request,'worker/viewedit.html')
		elif request.user.profile.loginas=="contractor":
			return render(request,'worker/profilecontractor.html')
		elif request.user.profile.loginas=="hirer":
			return render(request,'search/hirer.html')
		else:
			return render(request,'login/form.html',{"form":form})
	else:
		return render(request,'login/form.html',{"form":form})

def register_view(request):
	if request.method == 'POST' and 'btn' in request.POST:
		username=request.POST.get('username',None)
		aadhar=request.POST.get('aadhar',None)
		if len(aadhar)!=12:
			warn="आधार संख्या में 12 अंक होने चाहिए| (Aadhaar must have 12 digits.)"
			return render(request,'login/register.html',{"warn":warn})
		if User.objects.filter(username=username).exists() or User.objects.filter(last_name=aadhar).exists() :
			warn="उपयोगकर्ता नाम या आधार संख्या पहले से मौजूद है| (Username or aadhaar number already exists.)"
			return render(request,'login/register.html',{"warn":warn})
		m=re.search('@',username)
		otp=random.randint(1000,9999)
		serial=random.randint(10,99)
		warn = " "
		if m is None:
			if len(username) ==10 and username.isdigit():
				try:
					resp, code = sendSMS('zYEK/M9i6YU-vALs7nvcB0g7B0wb1YNkSOXaBEY4GS','91'+username,'TXTLCL','From Apna Rozgar OTP('+str(serial)+'): '+str(otp))
					res=resp.decode('utf-8')
					abcd=re.search('success',res)

					#aaa=sms(phno='8601867011',passwd='Ram2003',message='From Apna Rozgar OTP('+str(serial)+'): '+str(otp),receivernum=username)
					#if aaa=="yes":

					if abcd:
						warn="ओटीपी आपके मोबाइल नंबर पर भेज दिया गया है| कृपया प्रतीक्षा करें, अगर आपको 2 मिनट के अंदर नहीं मिला तो ओटीपी को फिर से भेजें"
					else:
						warn="आपका मोबाइल नंबर गलत है या एसएमएस भेजना विफल हो गया है|"
						return render(request,'login/register.html',{"warn":warn})
					
				except:
					warn="आपका मोबाइल नंबर गलत है या एसएमएस भेजना विफल हो गया है|"
					return render(request,'login/register.html',{"warn":warn})

			else:
				warn="मोबाइल नंबर गलत है।| (Mobile number is incorrect.)"
				return render(request,'login/register.html',{"warn":warn})

		else:
			try:
				email=EmailMessage('अपना रोज़ागर से ओटीपी (OTP From Apna Rozgar):', 'अपना रोज़ागर (Apna Rozgar) में आपका स्वागत है| अपना रोज़ागर से ओटीपी ( OTP)('+str(serial)+'): '+str(otp), to=[username])
				email.send()
				warn="ओटीपी आपके ईमेल पर भेज दिया गया है| कृपया प्रतीक्षा करें अगर आपको 2 मिनट के अंदर नहीं मिला तो ओटीपी को फिर से भेजें"
			except:
				warn="आपका ईमेल गलत है या ईमेल भेजना विफल हो गया है|"
				return render(request,'login/register.html',{"warn":warn})

		data=Registration_otp(username=username,aadhar=aadhar,otp=str(otp))
		data.save()			
		return render(request,'login/register1.html',{"mobile":username,"aadhar":aadhar,"warn":warn,'otp':str(serial)})

	elif request.method == 'POST' and 'btn1' in request.POST:
		mobile=request.POST.get('username')
		aadhar=request.POST.get('aadhar',None)
		otp2=request.POST.get('otp')
		otp1=Registration_otp.objects.get(username=mobile)
		password=request.POST.get('password',None)
		if not password:
			warn = "कृपया अपना पासवर्ड दर्ज करें।"
			return render(request,'login/register1.html',{"mobile":mobile,"aadhar":aadhar,"warn":warn})		
		if otp2==otp1.otp:
			otp1.delete()
			warn=" "
			form = UserRegisterForm(request.POST)
			user = form.save(commit = False)
			user.set_password(password)
			user.last_name=aadhar
			user.save()
			return render(request,'login/register2.html')
		else:
			warn="ओटीपी का मिलान नहीं हुआ|(OTP does not match.)"
			return render(request,'login/register1.html',{"mobile":mobile,"aadhar":aadhar,"warn":warn})
	else:
		warn=""
		return render(request,'login/register.html',{"warn":warn})


def logout_view(request):
	form = UserLoginForm(request.POST or None)
	logout(request)
	return render(request,'login/logout.html')

def profile_view(request):
	if request.user.username:
		if request.method=="POST" and (request.user.profile.loginas=="worker" or request.user.profile.loginas=="contractor"):
			address=request.POST.get('address',None)
			lat=request.POST.get('lat',None)
			lng=request.POST.get('lng',None)
			time=request.POST.get('time',None)
			sms=request.POST.get('sms',None)
			warn1 = " "
			if address!="N":
				data=Current_location(username=request.user.username,address=address,lat=lat,lng=lng,time=time)
				data.save()
				sms="वर्तमान स्थान को सफलतापूर्वक रिकॉर्ड किया गया: "
				warn1 = "" + address
			return render(request,'worker/viewedit.html',{'warn':sms, 'warn1': warn1})

		else:
			if request.user.profile.loginas=="worker" :        
				return render(request,'worker/viewedit.html')
			elif request.user.profile.loginas=="contractor":
				return render(request,'worker/profilecontractor.html')
			elif request.user.profile.loginas=="hirer":
				return render(request,'search/hirer.html')
			else:
				warn="कृपया पहले  लॉगिन करें"
				return render(request,'login/form.html',{'warn':warn})
	else:
		warn="कृपया पहले  लॉगिन करें"
		return render(request,'login/form.html',{'warn':warn})


def forgot_password_view(request):
	if request.method == 'POST' and 'btn' in request.POST:
		username=request.POST.get('username',None)
		if not User.objects.filter(username=username).exists():
			warn="उपयोगकर्ता नाम मौजूद नहीं है। कृपया इसे जांचें और पुनः प्रयास करें। (Username does not exist. Please check it and try again)"
			return render(request,'login/forgot.html',{"warn":warn})
		m=re.search('@',username)
		otp=random.randint(1000,9999)
		serial=random.randint(10,99)
		warn = " "
		if m is None:
			if len(username) ==10 and username.isdigit():
				try:
					resp, code = sendSMS('zYEK/M9i6YU-vALs7nvcB0g7B0wb1YNkSOXaBEY4GS','91'+username,'TXTLCL','From Apna Rozgar OTP('+str(serial)+'):- '+str(otp))
					res=resp.decode('utf-8')
					abcd=re.search('success',res)

					#aaa=sms(phno='8601867011',passwd='Ram2003',message='From Apna Rozgar OTP('+str(serial)+'): '+str(otp),receivernum=username)
					#if aaa=="yes":

					if abcd:
						warn="ओटीपी आपके मोबाइल नंबर पर भेज दिया गया है| कृपया प्रतीक्षा करें अगर आपको 2 मिनट के अंदर नहीं मिला तो ओटीपी को फिर से भेजें"
					else:
						warn="आपका मोबाइल नंबर गलत है या एसएमएस भेजना विफल हो गया है|"
						return render(request,'login/forgot.html',{"warn":warn})
				except:
					warn="आपका मोबाइल नंबर गलत है या एसएमएस भेजना विफल हो गया है|"
					return render(request,'login/forgot.html',{"warn":warn})

			else:
				warn="मोबाइल नंबर गलत है।| (Mobile number is incorrect.)"
				return render(request,'login/forgot.html',{"warn":warn})

		else:
			try:
				email=EmailMessage('अपना रोज़ागर से ओटीपी (OTP From Apna Rozgar):', 'अपना रोज़ागर (Apna Rozgar) में आपका स्वागत है| अपना रोज़ागर से ओटीपी ( OTP)('+str(serial)+'):- '
					+str(otp), to=[username])
				email.send()
				otpdata=""
				warn="ओटीपी आपके ईमेल पर भेज दिया गया है| कृपया प्रतीक्षा करें ,अगर आपको 2 मिनट के अंदर नहीं मिला तो ओटीपी को फिर से भेजें"
			except:
				warn="आपका ईमेल गलत है या ईमेल भेजना विफल हो गया है|"
				return render(request,'login/forgot.html',{"warn":warn})

		data=Registration_otp(username=username,otp=str(otp))
		data.save()			
		return render(request,'login/forgot1.html',{"mobile":username,"warn":warn,'otp':str(serial)})

	elif request.method == 'POST' and 'btn1' in request.POST:
		mobile=request.POST.get('username')
		otp2=request.POST.get('otp')
		otp1=Registration_otp.objects.get(username=mobile)
		password=request.POST.get('password',None)
		if not password:
			warn = "कृपया अपना पासवर्ड दर्ज करें।"
			return render(request,'login/forgot1.html',{"mobile":mobile,"warn":warn})	
		if otp2==otp1.otp:
			otp1.delete()
			warn=" "
			#form = UserRegisterForm(request.POST)
			#user = form.save(commit = False)
			user = User.objects.get(username=mobile)
			password=request.POST.get('password',None)
			user.set_password(password)
			user.save()
			return render(request,'login/forgot2.html')
		else:
			warn="ओटीपी का मिलान नहीं हुआ|(OTP does not match.)"
			return render(request,'login/forgot1.html',{"mobile":mobile,"warn":warn})
	else:
		warn=""
		return render(request,'login/forgot.html',{"warn":warn})


def change_password_view(request):
	if request.method == 'POST' and 'btn' in request.POST:
		username=request.POST.get('username',None)
		if not User.objects.filter(username=username).exists():
			warn="उपयोगकर्ता नाम मौजूद नहीं है। कृपया इसे जांचें और पुनः प्रयास करें। (Username does not exist. Please check it and try again)"
			return render(request,'login/forgot.html',{"warn":warn})
		m=re.search('@',username)
		otp=random.randint(1000,9999)
		serial=random.randint(10,99)
		warn = " "
		if m is None:
			if len(username) ==10 and username.isdigit():
				try:
					resp, code = sendSMS('zYEK/M9i6YU-vALs7nvcB0g7B0wb1YNkSOXaBEY4GS','91'+username,'TXTLCL','From Apna Rozgar OTP('+str(serial)+'):- '+str(otp))
					res=resp.decode('utf-8')
					abcd=re.search('success',res)

					#aaa=sms(phno='8601867011',passwd='Ram2003',message='From Apna Rozgar OTP('+str(serial)+'): '+str(otp),receivernum=username)
					#if aaa=="yes":

					if abcd:
						warn="ओटीपी आपके मोबाइल नंबर पर भेज दिया गया है| कृपया प्रतीक्षा करें, अगर आपको 2 मिनट के अंदर नहीं मिला तो ओटीपी को फिर से भेजें"
					else:
						warn="आपका मोबाइल नंबर गलत है या एसएमएस भेजना विफल हो गया है|"
						return render(request,'login/forgot.html',{"warn":warn})
				except:
					warn="आपका मोबाइल नंबर गलत है या एसएमएस भेजना विफल हो गया है|"
					return render(request,'login/forgot.html',{"warn":warn})

			else:
				warn="मोबाइल नंबर गलत है।| (Mobile number is incorrect.)"
				return render(request,'login/forgot.html',{"warn":warn})

		else:
			try:
				email=EmailMessage('अपना रोज़ागर से ओटीपी (OTP From Apna Rozgar):', 'अपना रोज़ागर (Apna Rozgar) में आपका स्वागत है| अपना रोज़ागर से ओटीपी ( OTP)('+str(serial)+'):- '+str(otp), to=[username])
				email.send()
				otpdata=""
				warn="ओटीपी आपके ईमेल पर भेज दिया गया है| कृपया प्रतीक्षा करें, अगर आपको 2 मिनट के अंदर नहीं मिला तो ओटीपी को फिर से भेजें"
			except:
				warn="आपका ईमेल गलत है या ईमेल भेजना विफल हो गया है|"
				return render(request,'login/forgot.html',{"warn":warn})

		data=Registration_otp(username=username,otp=str(otp))
		data.save()			
		return render(request,'login/forgot1.html',{"mobile":username,"warn":warn,'otp':str(serial)})

	elif request.method == 'POST' and 'btn1' in request.POST:
		mobile=request.POST.get('username')
		otp2=request.POST.get('otp')
		otp1=Registration_otp.objects.get(username=mobile)
		password=request.POST.get('password',None)
		if not password:
			warn = "कृपया अपना पासवर्ड दर्ज करें।"
			return render(request,'login/forgot1.html',{"mobile":mobile,"warn":warn})	
		if otp2==otp1.otp:
			otp1.delete()
			warn=" "
			#form = UserRegisterForm(request.POST)
			#user = form.save(commit = False)
			user = User.objects.get(username=mobile)
			password=request.POST.get('password',None)
			user.set_password(password)
			user.save()
			return render(request,'login/forgot2.html')
		else:
			warn="ओटीपी का मिलान नहीं हुआ|(OTP does not match.)"
			return render(request,'login/forgot1.html',{"mobile":mobile,"warn":warn})
	else:
		warn=""
		return render(request,'login/forgot.html',{"warn":warn})

def workrequest(request):
	if request.user.username:
		if request.method=="POST" and ('hhire' in request.POST or 'hchire' in request.POST ):
			post_id=request.POST.get('post_id')
			user_id=request.POST.get('user_id')
			start_date=request.POST.get('start_date')
			end_date=request.POST.get('end_date')
			page=request.POST.get('page')
			pq=Status.objects.filter(post_id=post_id,user_id=user_id)
			warn=""
			if len(pq)!=0:
				for pqr in pq:
					
					if 'hhire' in request.POST :
						r=Status.objects.filter(user_id=user_id,confirm='a',target=pqr.target)
						p=r.filter(Q(start_date__lte=start_date,end_date__gte=start_date)|Q(start_date__lte=end_date,end_date__gte=end_date)|Q(start_date__lte=start_date,end_date__gte=end_date)|Q(start_date__gte=start_date,end_date__lte=end_date))
						if len(p)==0:
							pqr.hirer_status=user_id
							pqr.confirm='a'
							pqr.save()

							#user=Profile.objects.get(user_id=user_id)
							
							#	resp, code = sendSMS('zYEK/M9i6YU-vALs7nvcB0g7B0wb1YNkSOXaBEY4GS',user.s_contact,'TXTLCL','Hirer '+pqr.hirer+' is accept your work request for work post id:- '+str(pqr.post_id)+' from '+ pqr.start_date +' to ' +pqr.end_date+'.' )
							#aaa=sms(phno='8840284384',passwd='K9532D',message='Hirer '+pqr.hirer+' is accept your work request for work post id:- '+str(pqr.post_id)+' from '+ pqr.start_date +' to ' +pqr.end_date+'.',receivernum=user.s_contact)


						elif pqr.confirm=='a':
							pqr.hirer_status=user_id
							pqr.save()

						else:
							warn="अब मजदूर इस तिथि पर उपलब्ध नहीं है।"
					if 'hchire' in request.POST:
						if (pqr.worker_status!=pqr.post_id) or pqr.confirm!='a':
							pqr.delete()
						else:
							pqr.hirer_status=0
							pqr.save()
			data=Status.objects.filter(userhirer=request.user.username)
			for select in data:
				if select.worker_status==select.post_id and select.hirer_status==select.user_id:
					select.temp='a'
					select.save()
				elif select.worker_status!=select.post_id and select.confirm=='a':
					select.temp='f'
					select.save()
				elif select.hirer_status!=select.user_id and select.confirm=='a':
					select.temp='e'
					select.save()
				elif select.worker_status==select.post_id:
					select.temp='c'
					select.save()
				elif select.hirer_status==select.user_id:
					select.temp='b'
					select.save()
				
				else:
					select.temp='d'
					select.save()        
			if len(data)==0:
				warn="वर्तमान में आपके लिए कोई अनुरोध नहीं है।"
			else:
				data=data.order_by('-status_id')
			pag = Paginator(data,3)
			if pag.num_pages < int(page):
				page=int(page)-1
			p = pag.page(int(page))
			return render(request,'search/workrequest.html',{'data':p,'warn':warn})
		elif request.method=="POST" and ('whire' in request.POST or 'wchire' in request.POST ):
			post_id=request.POST.get('post_id')
			user_id=request.POST.get('user_id')
			start_date=request.POST.get('start_date')
			end_date=request.POST.get('end_date')
			pq=Status.objects.filter(post_id=post_id,user_id=user_id)
			page=request.POST.get('page')
			if request.user.profile.loginas=="contractor":
					target='b'
			else:
					target='a'
			warn=""
			if len(pq)!=0:
				for pqr in pq:
					if 'whire' in request.POST :
						r=Status.objects.filter(user_id=user_id,confirm='a',target=target)
						p=r.filter(Q(start_date__lte=start_date,end_date__gte=start_date)|Q(start_date__lte=end_date,end_date__gte=end_date)|Q(start_date__lte=start_date,end_date__gte=end_date)|Q(start_date__gte=start_date,end_date__lte=end_date))
						if len(p)==0:
							pqr.worker_status=post_id
							pqr.confirm='a'
							pqr.save()

							#user=Posts.objects.get(post_id=post_id)
							
							#	resp, code = sendSMS('zYEK/M9i6YU-vALs7nvcB0g7B0wb1YNkSOXaBEY4GS',user.s_contact,'TXTLCL','Worker/contractor '+pqr.worker+' is accept your work request for work post id:- '+str(pqr.post_id)+' from '+ pqr.start_date +' to ' +pqr.end_date+'.' )
							#aaa=sms(phno='8840284384',passwd='K9532D',message='Worker/contractor '+pqr.worker+' is accept your work request for work post id:- '+str(pqr.post_id)+' from '+ pqr.start_date +' to ' +pqr.end_date+'.',receivernum=user.s_contact)

						elif pqr.confirm=='a':
							pqr.worker_status=post_id
							pqr.save()
						else:
							warn="आप इस तिथि पर उपलब्ध नहीं हैं।"
					if 'wchire' in request.POST:
						if (pqr.hirer_status!= pqr.user_id) or pqr.confirm!='a':
							pqr.delete()
						else:
							pqr.worker_status=0
							pqr.save()
			data=Status.objects.filter(userworker=request.user.username,target=target)
			for select in data:
				if select.worker_status==select.post_id and select.hirer_status==select.user_id:
					select.temp='a'
					select.save()
				elif select.worker_status!=select.post_id and select.confirm=='a':
					select.temp='e'
					select.save()
				elif select.hirer_status!=select.user_id and select.confirm=='a':
					select.temp='f'
					select.save()
				elif select.worker_status==select.post_id:
					select.temp='b'
					select.save()
				elif select.hirer_status==select.user_id:
					select.temp='c'
					select.save()
				
				else:
					select.temp='d'
					select.save()        
			
			if len(data)==0:
				warn="वर्तमान में आपके लिए कोई अनुरोध नहीं है।"
			else:
				data=data.order_by('-status_id')
			pag = Paginator(data,3)
			if pag.num_pages < int(page):
				page=int(page)-1
			p = pag.page(int(page))
			return render(request,'worker/workrequest.html',{'data':p,'warn':warn})
		else: 	
			if request.user.profile.loginas=="worker" or request.user.profile.loginas=="contractor":
				if request.user.profile.loginas=="contractor":
					target='b'
				else:
					target='a'
				data=Status.objects.filter(userworker=request.user.username,target=target)        
				for select in data:
					if select.worker_status==select.post_id and select.hirer_status==select.user_id:
						select.temp='a'
						select.save()
					elif select.worker_status!=select.post_id and select.confirm=='a':
						select.temp='e'
						select.save()
					elif select.hirer_status!=select.user_id and select.confirm=='a':
						select.temp='f'
						select.save()
					elif select.worker_status==select.post_id:
						select.temp='b'
						select.save()
					elif select.hirer_status==select.user_id:
						select.temp='c'
						select.save()
					
					else:
						select.temp='d'
						select.save()        
				warn=""
				if len(data)==0:
					warn="वर्तमान में आपके लिए कोई अनुरोध नहीं है।"
				else:
					data=data.order_by('-status_id')
				pag = Paginator(data,3)
				page = request.GET.get('page',None)
				if not page:
					page='1'
				p = pag.page(int(page))
				return render(request,'worker/workrequest.html',{'data':p,'warn':warn})

			
			elif request.user.profile.loginas=="hirer":
				data=Status.objects.filter(userhirer=request.user.username)
				for select in data:
					if select.worker_status==select.post_id and select.hirer_status==select.user_id:
						select.temp='a'
						select.save()
					elif select.worker_status!=select.post_id and select.confirm=='a':
						select.temp='f'
						select.save()
					elif select.hirer_status!=select.user_id and select.confirm=='a':
						select.temp='e'
						select.save()
					elif select.worker_status==select.post_id:
						select.temp='c'
						select.save()
					elif select.hirer_status==select.user_id:
						select.temp='b'
						select.save()
					
					else:
						select.temp='d'
						select.save()        
				warn=""
				if len(data)==0:
					warn="वर्तमान में आपके लिए कोई अनुरोध नहीं है।"
				else:
					data=data.order_by('-status_id')
				pag = Paginator(data,3)
				page = request.GET.get('page',None)
				if not page:
					page='1'
				p = pag.page(int(page))
				return render(request,'search/workrequest.html',{'data':p,'warn':warn})
	else:
		warn="कृपया पहले  लॉगिन करें"
		return render(request,'login/form.html',{'warn':warn})

