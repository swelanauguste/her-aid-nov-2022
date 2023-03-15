from django import forms
from django.forms import NumberInput, Textarea, TextInput

from .models import Donation, Subscribe, Volunteer

class1 = "border-0 border-bottom border-dark bg-pink rounded-0"


class SubscribeCreateForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ("email",)


class UnSubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ("email",)


class VolunteerCreateForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = "__all__"
        widgets = {
            "name": TextInput(
                attrs={
                    "class": class1,
                    "type": "text",
                }
            ),
            "email": TextInput(
                attrs={
                    "class": class1,
                    "type": "email",
                }
            ),
            "phone": TextInput(
                attrs={
                    "class": class1,
                }
            ),
            "how": Textarea(attrs={"rows": "4", "class": class1}),
        }


class DonationCreateForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ["name", "email", "phone", "amount", "note"]
        widgets = {
            "name": TextInput(
                attrs={
                    "class": class1,
                    "type": "text",
                }
            ),
            "email": TextInput(
                attrs={
                    "class": class1,
                    "type": "email",
                }
            ),
            "phone": TextInput(
                attrs={
                    "class": class1,
                }
            ),
            "amount": NumberInput(
                attrs={
                    "class": class1,
                    "min": "0.5",
                }
            ),
            "note": Textarea(attrs={"rows": "4", "class": class1}),
        }
