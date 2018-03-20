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
from django.core.mail import EmailMessage
import re
import string
def smss(request):
	
	q=sms('8840284384','K9532D')
	a=random.randint(1000,9999)
	q.send('8267962765','From Apna Rozgar OTP:'+str(a))
	return render(request,'login/form.html')
def aboutus(request):
	return 
	
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
			warn="आधार संख्या में 12 अंक होने चाहिए| (Aadhar number have 12 digits.)"
			return render(request,'login/register.html',{"warn":warn})
		if User.objects.filter(username=username).exists() or User.objects.filter(last_name=aadhar).exists() :
			warn="उपयोगकर्ता नाम या आधार संख्या पहले से मौजूद है| (Username or aadhar number is already exists.)"
			return render(request,'login/register.html',{"warn":warn})
		m=re.search('@',username)
		otp=random.randint(1000,9999)
		if m is None:
			if len(username) ==10 and username.isdigit():
				try:
<<<<<<< HEAD
					q=sms('8601867011','Ram2003')
					q.send(username,'Welcome to Apna Rozgar. Your Registration  OTP is: '+str(otp))
					n=q.msgSentToday()
					q.logout()
=======
					q=sms('8840284384','K9532D')
					q.send(username,'From Apna Rozgar, Your OTP is: '+str(otp))
>>>>>>> 4b5e009239ec15c413c92aa9cf72143749b259ac
					otpdata=""
					warn="ओटीपी आपके मोबाइल नंबर पर भेज दिया गया है|(OTP has been sent to your Mobile number.)"
				except:
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
			warn="ओटीपी का मिलान नहीं हुआ|(OTP did not matched.)"
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
	return HttpResponse("<h2>HEY! forgot password</h2>")
def change_password_view(request):
	return HttpResponse("<h2>HEY! change password</h2>")

