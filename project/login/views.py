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
from .way2sms import sms
import random
from .forms import UserLoginForm, UserRegisterForm
from .models import LoginAs,Registration_otp
from search.models import Status
from django.core.mail import EmailMessage
import re
import string
def smss(request):
	
	q=sms('8840284384','K9532D')
	a=random.randint(1000,9999)
	q.send('8601867011','From Apna Rozgar OTP:'+str(a))
	return render(request,'login/form.html')

def aboutus(request):
	return render(request,'login/aboutus.html')
	
def login_view(request):
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		loginas1 = form.cleaned_data.get("loginas")
		user = authenticate(username = username, password = password)
		if not user or not user.check_password(password) or not user.is_active:
			warn="उपयोगकर्ता नाम/ पासवर्ड गलत है । कृपया पुन: प्रयास करें|(Wrong username or password. Try again.)"
			return render(request,'login/form.html',{"form":form,"warn":warn})
		login(request,user)
		request.user.is_authenticated()
		data=LoginAs(username=username,loginas=loginas1)
		data.save()
		if loginas1=="worker":
			return render(request,'worker/viewedit.html')
		else:
			return render(request,'search/hirer.html')
	elif request.user.username:
		value=LoginAs.objects.get(username=request.user.username)
		if value.loginas=="worker":        
			return render(request,'worker/viewedit.html')
		else:
			return render(request,'search/hirer.html')
	else:
		return render(request,'login/form.html',{"form":form})

def register_view(request):
	if request.method == 'POST' and 'btn' in request.POST:
		username=request.POST.get('username',None)
		aadhar=request.POST.get('aadhar',None)
		if len(aadhar)!=12:
			warn="आधार संख्या में 12 अंक होने चाहिए| (Aadhaar number must have 12 digits.)"
			return render(request,'login/register.html',{"warn":warn})
		if User.objects.filter(username=username).exists() or User.objects.filter(last_name=aadhar).exists() :
			warn="उपयोगकर्ता नाम या आधार संख्या पहले से मौजूद है| (Username or aadhaar number already exists.)"
			return render(request,'login/register.html',{"warn":warn})
		m=re.search('@',username)
		otp=random.randint(1000,9999)
		warn = " "
		if m is None:
			if len(username) ==10 and username.isdigit():
				#try:
				#	q=sms('8840284384','K9532D')
				#	q.send(username,'From Apna Rozgar, Your OTP is: '+str(otp))
				#	otpdata=""
				#	warn="ओटीपी आपके मोबाइल नंबर पर भेज दिया गया है|(OTP has been sent to your Mobile number.)"
				#except:
					otpdata=str(otp)
					warn="आपका मोबाइल नंबर गलत है या एसएमएस भेजना विफल हो गया है|"

			else:
				warn="मोबाइल नंबर गलत है।| (Mobile number is incorrect.)"
				return render(request,'login/register.html',{"warn":warn})

		else:
			try:
				email=EmailMessage('अपना रोज़ागर से ओटीपी (OTP From Apna Rozgar):', 'अपना रोज़ागर (Apna Rozgar) में आपका स्वागत है| अपना रोज़ागर से ओटीपी ( OTP): '+str(otp), to=[username])
				email.send()
				otpdata=""
				warn="ओटीपी आपके ईमेल पर भेज दिया गया है|(OTP has been sent to your Email-id.)"
			except:
				otpdata=str(otp)
				warn="आपका ईमेल गलत है या ईमेल भेजना विफल हो गया है|"

		data=Registration_otp(username=username,aadhar=aadhar,otp=str(otp))
		data.save()			
		return render(request,'login/register1.html',{"mobile":username,"aadhar":aadhar,"warn":warn,"otp":otpdata})

	elif request.method == 'POST' and 'btn1' in request.POST:
		mobile=request.POST.get('username')
		otp2=request.POST.get('otp')
		otp1=Registration_otp.objects.get(username=mobile)
		if otp2==otp1.otp:
			otp1.delete()
			warn=" "
			form = UserRegisterForm(request.POST)
			user = form.save(commit = False)
			password=request.POST.get('password',None)
			user.set_password(password)
			user.save()
			return render(request,'login/register2.html')
		else:
			warn="ओटीपी का मिलान नहीं हुआ|(OTP does not match.)"
			return render(request,'login/register1.html',{"mobile":mobile,"warn":warn})
	else:
		warn=""
		return render(request,'login/register.html',{"warn":warn})


def logout_view(request):
	form = UserLoginForm(request.POST or None)
	logout(request)
	return render(request,'login/logout.html')

def profile_view(request):
	value=LoginAs.objects.get(username=request.user.username)
	if value.loginas=="worker":        
		return render(request,'worker/viewedit.html')
		#return HttpResponseRedirect('worker/viewprofile')
	else:
		return render(request,'search/hirer.html')

def forgot_password_view(request):
	if request.method == 'POST' and 'btn' in request.POST:
		username=request.POST.get('username',None)
		if not User.objects.filter(username=username).exists():
			warn="उपयोगकर्ता नाम मौजूद नहीं है। कृपया इसे जांचें और पुनः प्रयास करें। (Username does not exist. Please check it and try again)"
			return render(request,'login/forgot.html',{"warn":warn})
		m=re.search('@',username)
		otp=random.randint(1000,9999)
		warn = " "
		if m is None:
			if len(username) ==10 and username.isdigit():
				#try:
				#	q=sms('8840284384','K9532D')
				#	q.send(username,'From Apna Rozgar, Your OTP is: '+str(otp))
				#	otpdata=""
				#	warn="ओटीपी आपके मोबाइल नंबर पर भेज दिया गया है|(OTP has been sent to your Mobile number.)"
				#except:
					otpdata=str(otp)
				#	warn="आपका मोबाइल नंबर गलत है या एसएमएस भेजना विफल हो गया है|"

			else:
				warn="मोबाइल नंबर गलत है।| (Mobile number is incorrect.)"
				return render(request,'login/forgot.html',{"warn":warn})

		else:
			try:
				email=EmailMessage('अपना रोज़ागर से ओटीपी (OTP From Apna Rozgar):', 'अपना रोज़ागर (Apna Rozgar) में आपका स्वागत है| अपना रोज़ागर से ओटीपी ( OTP): '+str(otp), to=[username])
				email.send()
				otpdata=""
				warn="ओटीपी आपके ईमेल पर भेज दिया गया है|(OTP has been sent to your Email-id.)"
			except:
				otpdata=str(otp)
				warn="आपका ईमेल गलत है या ईमेल भेजना विफल हो गया है|"

		data=Registration_otp(username=username,otp=str(otp))
		data.save()			
		return render(request,'login/forgot1.html',{"mobile":username,"warn":warn,"otp":otpdata})

	elif request.method == 'POST' and 'btn1' in request.POST:
		mobile=request.POST.get('username')
		otp2=request.POST.get('otp')
		otp1=Registration_otp.objects.get(username=mobile)
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
		warn = " "
		if m is None:
			if len(username) ==10 and username.isdigit():
				#try:
				#	q=sms('8840284384','K9532D')
				#	q.send(username,'From Apna Rozgar, Your OTP is: '+str(otp))
				#	otpdata=""
				#	warn="ओटीपी आपके मोबाइल नंबर पर भेज दिया गया है|(OTP has been sent to your Mobile number.)"
				#except:
					otpdata=str(otp)
				#	warn="आपका मोबाइल नंबर गलत है या एसएमएस भेजना विफल हो गया है|"

			else:
				warn="मोबाइल नंबर गलत है।| (Mobile number is incorrect.)"
				return render(request,'login/forgot.html',{"warn":warn})

		else:
			try:
				email=EmailMessage('अपना रोज़ागर से ओटीपी (OTP From Apna Rozgar):', 'अपना रोज़ागर (Apna Rozgar) में आपका स्वागत है| अपना रोज़ागर से ओटीपी ( OTP): '+str(otp), to=[username])
				email.send()
				otpdata=""
				warn="ओटीपी आपके ईमेल पर भेज दिया गया है|(OTP has been sent to your Email-id.)"
			except:
				otpdata=str(otp)
				warn="आपका ईमेल गलत है या ईमेल भेजना विफल हो गया है|"

		data=Registration_otp(username=username,otp=str(otp))
		data.save()			
		return render(request,'login/forgot1.html',{"mobile":username,"warn":warn,"otp":otpdata})

	elif request.method == 'POST' and 'btn1' in request.POST:
		mobile=request.POST.get('username')
		otp2=request.POST.get('otp')
		otp1=Registration_otp.objects.get(username=mobile)
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
	if request.method=="POST" and ('hhire' in request.POST or 'hchire' in request.POST ):
		post_id=request.POST.get('post_id')
		user_id=request.POST.get('user_id')
		pqr=Status.objects.get(post_id=post_id,user_id=user_id)
		if 'hchire' in request.POST :
			pqr.hirer_status=0
		else:
			pqr.hirer_status=user_id
			pqr.save()
		if 'hchire' in request.POST and pqr.worker_status!=post_id:
			pqr.delete()
		data=Status.objects.filter(userhirer=request.user.username)
		for select in data:
			if select.worker_status==select.post_id and select.hirer_status==select.user_id:
				select.temp='a'
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
			warn="no request"
		return render(request,'search/workrequest.html',{'data':data,'warn':warn})
	elif request.method=="POST" and ('whire' in request.POST or 'wchire' in request.POST ):
		post_id=request.POST.get('post_id')
		user_id=request.POST.get('user_id')
		pqr=Status.objects.get(post_id=post_id,user_id=user_id)
		if 'wchire' in request.POST :
			pqr.worker_status=0
		else:
			pqr.worker_status=post_id
		pqr.save()
		if 'wchire' in request.POST and pqr.hirer_status!=user_id:
			pqr.delete()
		data=Status.objects.filter(userworker=request.user.username)
		for select in data:
			if select.worker_status==select.post_id and select.hirer_status==select.user_id:
				select.temp='a'
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
			warn="no request"
		return render(request,'worker/workrequest.html',{'data':data,'warn':warn})
	else: 	
		value=LoginAs.objects.get(username=request.user.username)
		if value.loginas=="worker":
			data=Status.objects.filter(userworker=request.user.username)        
			for select in data:
				if select.worker_status==select.post_id and select.hirer_status==select.user_id:
					select.temp='a'
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
				warn="no request"
			return render(request,'worker/workrequest.html',{'data':data,'warn':warn})

		
		else:
			data=Status.objects.filter(userhirer=request.user.username)
			for select in data:
				if select.worker_status==select.post_id and select.hirer_status==select.user_id:
					select.temp='a'
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
				warn="no request"
			return render(request,'search/workrequest.html',{'data':data,'warn':warn})

