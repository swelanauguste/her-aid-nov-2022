from django.contrib import admin

from .models import Donation, Volunteer

admin.site.register(Donation)
admin.site.register(Volunteer)