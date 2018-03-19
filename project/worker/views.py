from django.shortcuts import render
from .forms import  ProfileForm1,ProfileForm2
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib.auth.models import User
from .models import Profile,location
import re
import urllib.request
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
