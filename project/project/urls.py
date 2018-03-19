"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from login.views import (login_view, register_view, logout_view,profile_view,forgot_password_view,change_password_view,smss)
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login',login_view,name = 'login'),
    url(r'^logout',logout_view,name = 'logout'),
    url(r'^sms',smss,name = 'sms'),
    url(r'^view',profile_view,name = 'view'),
    url(r'^register',register_view,name = 'register'),
     url(r'^forgot_password',forgot_password_view,name = 'forgot_password'),
      url(r'^change_password',change_password_view,name = 'change_password'),
    url(r'^worker/',include('worker.urls')),
    url(r'^login',login_view,name = 'login'),
    url(r'^search',include('search.urls'))
    
]
