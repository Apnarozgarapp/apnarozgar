from django.contrib import admin

from worker.models import Profile,location,Current_location,Contractor

admin.site.register(Profile)
admin.site.register(location)
admin.site.register(Current_location)
admin.site.register(Contractor)

