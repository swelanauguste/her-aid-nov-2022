from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Referral

class Referral(TemplateView):
    referrals = Referral.objects.all()
    extra_context = {"referrals": referrals}
    template_name = 'gethelp/referral.html'