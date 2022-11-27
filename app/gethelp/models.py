from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return f"{self.category.title()}"


class District(models.Model):
    district = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ("district",)

    def __str__(self):
        return f"{self.district}"


class Location(models.Model):
    location = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ["id"]
        unique_together = ('location', 'district',)

    def __str__(self):
        return f"{self.district.district}, {self.location}"


class Referral(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, default=1
    )
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    tel = models.CharField(max_length=100)
    tel1 = models.CharField(max_length=100, blank=True)
    tel2 = models.CharField(max_length=100, blank=True)
    hotline = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    funded_by = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    service = models.CharField(max_length=100)
    open_hours = models.CharField(max_length=100)
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
