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


def smss(request):
	
	email=EmailMessage('hello', 'body goes here', to=['ramnarayanamethi@gmail.com'])
	email.send()
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
			warn="उपयोगकर्ता नाम/ पासवर्ड गलत है । कृपया पुन: प्रयास करें|"
			return render(request,'login/form.html',{"form":form,"warn":warn})
		login(request,user)
		request.user.is_authenticated()
		data=LoginAs(username=username,loginas=loginas1)
		data.save()
		if loginas1=="worker":
			return render(request,'worker/viewedit.html')
				#return HttpResponseRedirect('/worker/')
		else:
			return render(request,'search/hirer.html')
	elif request.user.username:
		value=LoginAs.objects.get(username=request.user.username)
		if value.loginas=="worker":        
			return render(request,'worker/viewedit.html')
			#return HttpResponseRedirect('worker/viewprofile')
		else:
			return render(request,'search/hirer.html')
	else:
		
		return render(request,'login/form.html',{"form":form})

def register_view(request):
	if request.method == 'POST' and 'btn' in request.POST:
		mobile=request.POST.get('username',None)
		if not User.objects.filter(username=mobile).exists():
			usernam=mobile[3:13]
			otp=random.randint(1000,9999)
			#q=sms('8840284384','K9532D')
			#q.send(usernam,'Welcome to APNA ROZGAR. Your registration OTP is: '+str(otp))
			#n=q.msgSentToday()
			#q.logout() 
			data=Registration_otp(username=mobile,otp=str(otp))
			data.save()			
			warn="ओटीपी आपके मोबाइल नंबर पर भेज दिया गया है|(OTP has been sent to your Mobile number.)"
			return render(request,'login/register1.html',{"mobile":mobile,"warn":warn,"otp":str(otp)})
		else:
			warn="मोबाइल नंबर पहले से मौजूद है|(Mobile number already exists.)"
			return render(request,'login/register.html',{"warn":warn})

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

