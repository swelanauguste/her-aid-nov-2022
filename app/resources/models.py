from django.db import models


class TypeOfAbuse(models.Model):
    title = models.CharField(max_length=100, unique=True)
    details = models.TextField()
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Screening(models.Model):
    question = models.TextField()
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question


class SignAndPrevention(models.Model):
    title = models.CharField(max_length=100, unique=True)
    details = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'signs and prevention'

    def __str__(self):
        return self.question
