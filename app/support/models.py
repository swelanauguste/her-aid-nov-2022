from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse
from django.conf import settings

class Volunteer(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=25, null=True)
    how = models.TextField(help_text="how do you want to support?")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    remain_anonymous = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("support:volunteer-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class Donation(models.Model):
    name = models.CharField(max_length=255)
    amount = models.DecimalField(decimal_places=2, max_digits=9)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=25, null=True)
    donated = models.BooleanField(default=False)
    note = models.TextField(blank=True)
    remain_anonymous = models.BooleanField(default=True)
    stripe_id = models.CharField(max_length=255, blank=True)
    check_out_id = models.CharField(max_length=255, blank=True)

    def get_absolute_url(self):
        return reverse("support:donation-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.name} made a donation of {self.amount}"

