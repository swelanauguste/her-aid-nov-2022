from django.shortcuts import render
from django.views.generic import TemplateView

from .models import WhatWeDo, FAQ, MythAndFact


class Home(TemplateView):
    faqs = FAQ.objects.all()
    myths_and_facts = MythAndFact.objects.all()
    extra_context = {"faqs": faqs, "myths_and_facts": myths_and_facts}
    template_name = "home/home.html"
