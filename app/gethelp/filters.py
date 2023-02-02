import django_filters
from django import forms
from .models import Category, Location, Referral, District


class ReferralFilter(django_filters.FilterSet):
    category = django_filters.ModelChoiceFilter(
        queryset=Category.objects.all(),
        label="Category",
        widget=forms.Select(
            attrs={
                "class": "rounded-pill",
                "onchange": "this.form.submit()",
                "empty_label": "Categories",
            }
        ),
    )

    location__district = django_filters.ModelChoiceFilter(
        queryset=District.objects.all(),
        label="Location",
        widget=forms.Select(
            attrs={
                "class": "rounded-pill",
                "onchange": "this.form.submit()",
            }
        ),
    )

    class Meta:
        model = Referral
        fields = ["category", "location__district"]
