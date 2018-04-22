from django.contrib import admin

# Register your models here.

from search.models import Posts,Status

admin.site.register(Posts)
admin.site.register(Status)
