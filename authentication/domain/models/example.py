from django.db import models

class Example(models.Model):
    description = models.CharField(max_length=250)
    other = models.CharField(max_length=100, null=True, blank=True)