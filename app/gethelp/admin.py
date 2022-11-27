from django.contrib import admin

from .models import Category, District, Location, Referral

admin.site.register(Referral)
admin.site.register(Category)
admin.site.register(District)
admin.site.register(Location)
