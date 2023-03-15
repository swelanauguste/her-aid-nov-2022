from django.contrib import admin

from .models import Donation, Subscribe, Volunteer

admin.site.register(Donation)
admin.site.register(Volunteer)
admin.site.register(Subscribe)
