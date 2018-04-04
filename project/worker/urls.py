from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^edit', views.update_profile),
    url(r'^seepost', views.viewpost),
    ]
