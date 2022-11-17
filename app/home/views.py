from django.shortcuts import render
from django.views.generic import TemplateView

from .models import FAQ, MythAndFact, WhatWeDo


class Home(TemplateView):
    faqs = FAQ.objects.all()
    myths_and_facts = MythAndFact.objects.all()
    extra_context = {"faqs": faqs, "myths_and_facts": myths_and_facts}
    template_name = "home/home.html"


class MobileHome(TemplateView):
    template_name = "home/mobile/mobile_home.html"
