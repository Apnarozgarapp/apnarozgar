from django.contrib import admin

# Register your models here.

from search.models import Posts,status

admin.site.register(Posts)
admin.site.register(status)
