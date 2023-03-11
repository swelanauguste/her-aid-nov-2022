from django import forms

from .models import Donate

class DonationCreateForm(forms.ModelForm):
    class Meta:
        model = Donate
        fields = ['name', 'email', 'phone', 'amount','note']