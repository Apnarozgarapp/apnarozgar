from django.conf.urls import url, include
from . import views

urlpatterns = [ url(r'^$', views.search_result, name = 'search'),
		url(r'^/',views.view_worker)
		]
