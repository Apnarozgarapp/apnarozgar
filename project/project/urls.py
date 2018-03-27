from django.conf.urls import include, url
from django.contrib import admin
from login.views import (login_view, register_view, logout_view,profile_view,forgot_password_view,change_password_view,smss, aboutus)

from search.views import (work_post,see_work_post)
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
    url(r'^search',include('search.urls')),
    url(r'^work_post',work_post,name = 'work_post'),
    url(r'^see_work_post',see_work_post,name = 'see_work_post'),
    url(r'^about_us',aboutus,name = 'about_us'),
    
]
