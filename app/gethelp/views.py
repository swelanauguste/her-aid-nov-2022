from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from .filters import ReferralFilter
from .models import Category, Referral

# class CategoryListView(ListView):
#     model = Category
#     template_name = "gethelp/referral.html"

#     def get_queryset(self, **kwargs):
#         qs = super().get_queryset(**kwargs)
#         print("qs", qs)
#         return qs.filter(id=self.kwargs["pk"])


class GetHelpViewMobile(TemplateView):
    template_name = "gethelp/mobile/get_help.html"


class Referral(ListView):
    queryset = Referral.objects.all()
    context_object_name = "referrals"
    template_name = "gethelp/referral.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ReferralFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.filterset.form
        return context
