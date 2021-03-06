from django.conf.urls import include, url
from django.contrib import admin
from login.views import (Developer, query,change_role,login_view, register_view, logout_view,profile_view,forgot_password_view,change_password_view,smss, aboutus,workrequest)
from search.views import (work_post,see_work_post,update,view_worker,done,search_result)
from worker.views import (viewpost,update_profile,detail_post,all_post,confirm_work,profile,feedback,payment_detail,payments,contractor_profile,cprofile)
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login',login_view,name = 'login'),
     url(r'^developer',Developer,name = 'developer'),
    url(r'^query',query,name = 'query'),
    url(r'^change_role',change_role,name = 'change_role'),
    url(r'^$',aboutus,name = 'about'),
    url(r'^logout',logout_view,name = 'logout'),
    url(r'^workrequest',workrequest,name = 'workrequest'),
    url(r'^contractor_profile',contractor_profile,name = 'contractor_profile'),
    url(r'^view',profile_view,name = 'view'),
    url(r'^register',register_view,name = 'register'),
    url(r'^forgot_password',forgot_password_view,name = 'forgot_password'),
    url(r'^change_password',change_password_view,name = 'change_password'),
    url(r'^worker/',include('worker.urls')),
    url(r'^login',login_view,name = 'login'),
    url(r'^profile',profile,name = 'profile'),
    url(r'^feedback',feedback,name = 'feedback'),
    url(r'^search',search_result,name='search_result'),
    url(r'^work_post',work_post,name = 'work_post'),
    url(r'^done',done,name = 'done'),
    url(r'^cprofile',cprofile,name = 'cprofile'),
    url(r'^payment_detail',payment_detail,name = 'payment_detail'),
    url(r'^confirm_work',confirm_work,name = 'confirm_work'),
    url(r'^hpay',payments,name = 'payments'),
    url(r'^detailpost',detail_post,name = 'detail_post'),
    url(r'^allpost',all_post,name = 'all_post'),
    url(r'^update',update,name = 'update'),
    url(r'^see_work_post',see_work_post,name = 'see_work_post'),
    url(r'^about',aboutus,name = 'about_us'),
    url(r'^seeworker',view_worker,name = 'view_worker'),
    url(r'^pupdate_profile',update_profile,name = 'update_profile'),
    url(r'^pview',viewpost,name = 'viewpost'),
]
