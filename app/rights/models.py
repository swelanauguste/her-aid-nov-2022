from django.db import models

class Right(models.Model):
    title = models.CharField(max_length=100, unique=True)
    sub_title = models.CharField(max_length=100, unique=True)
    details = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    