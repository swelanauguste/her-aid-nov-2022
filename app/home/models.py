from django.db import models


class WhatWeDo(models.Model):
    title = models.CharField(max_length=50, unique=True)
    details = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'what we do'

    def __str__(self):
        return self.title


class FAQ(models.Model):
    question = models.CharField(max_length=50, unique=True)
    details = models.TextField()
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question


class MythAndFact(models.Model):
    title = models.CharField(max_length=50, unique=True)
    details = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'myths and facts'

    def __str__(self):
        return self.title
