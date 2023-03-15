from django.db import models


class WhatWeDo(models.Model):
    title = models.TextField(unique=True)
    details = models.TextField()
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "what we do"

    # def get_sentence_case(self):
    #     output = ""
    #     isFirstWord = True

    #     for c in self.details:
    #         if isFirstWord and not c.isspace():
    #             c = c.upper()
    #             isFirstWord = False
    #         elif not isFirstWord and c in ".!?":
    #             isFirstWord = True
    #         else:
    #             c = c.lower()

    #         output = output + c

    def __str__(self):
        return self.title


class FAQ(models.Model):
    question = models.TextField(unique=True)
    details = models.TextField()
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question


class MythAndFact(models.Model):
    title = models.TextField(unique=True)
    details = models.TextField()
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "myths and facts"

    def __str__(self):
        return self.title
