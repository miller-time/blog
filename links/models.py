from django.db import models

class Link(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
