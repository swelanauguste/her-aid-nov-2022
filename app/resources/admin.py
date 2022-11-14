from django.contrib import admin

from .models import TypeOfAbuse, Screening, SignAndPrevention

admin.site.register(TypeOfAbuse)
admin.site.register(Screening)
admin.site.register(SignAndPrevention)