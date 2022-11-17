from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=50, unique=True)
    
    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return F"{self.category.title()} ({self.id})"


class Referral(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, default=1)
    district = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)
    tel1 = models.CharField(max_length=50, blank=True)
    tel2 = models.CharField(max_length=50, blank=True)
    hotline = models.CharField(max_length=50)
    organization = models.CharField(max_length=50)
    funded_by = models.CharField(max_length=50)
    sector = models.CharField(max_length=50)
    service = models.CharField(max_length=50)
    open_hours = models.CharField(max_length=50)
    remote_services = models.BooleanField(default=1)
    for_women = models.BooleanField(default=1)
    for_men = models.BooleanField(default=1)
    for_girls = models.BooleanField(default=1)
    for_boys = models.BooleanField(default=1)
    for_seniors = models.BooleanField(default=1)
    for_homeless = models.BooleanField(default=1)
    for_disabled = models.BooleanField(default=1)
    for_lgbt = models.BooleanField(default=1)
    for_refugees = models.BooleanField(default=1)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name
