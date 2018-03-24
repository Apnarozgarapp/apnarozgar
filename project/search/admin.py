from django.contrib import admin

# Register your models here.

from search.models import Posts_of_work,status

admin.site.register(Posts_of_work)
admin.site.register(status)
