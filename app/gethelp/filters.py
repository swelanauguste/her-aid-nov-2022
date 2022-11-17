import django_filters

from .models import Referral

class ReferralFilter(django_filters.FilterSet):
    class Meta:
        model = Referral
        fields = ['category',]