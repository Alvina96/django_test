from django.contrib import admin
from . models import application
from . models import apikey

admin.site.register(application)
admin.site.register(apikey)
# Register your models here.
