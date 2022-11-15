from django.shortcuts import render

from django.views.generic import TemplateView

from .models import Right

class Right(TemplateView):
    rights = Right.objects.all()
    extra_context = {
        'rights': rights
    }
    template_name = 'rights/rights.html'