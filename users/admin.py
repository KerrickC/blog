from django.contrib import admin
from .models import Profile
from . import models
# Register your models here.
#Need to do this each time you add a model so it is accessible to admin

admin.site.register(Profile)



