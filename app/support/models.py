from django.core.validators import MinValueValidator
from django.db import models


class Volunteer(models.Model):
    name = models.CharField(max_length=255)
    contact = models.TextField(help_text="email, tel, mobile")
    how = models.TextField(help_text="how do you want to support?")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    remain_anonymous = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Donate(models.Model):
    name = models.CharField(max_length=255)
    amount = models.DecimalField(
        default=5.00, decimal_places=2, max_digits=9, validators=[MinValueValidator(1)]
    )
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=25, null=True)
    donated = models.BooleanField(default=False)
    note = models.TextField(blank=True)
    remain_anonymous = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} made a donation of {self.amount}"