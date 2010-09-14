from django.db import models
from django import forms

class Scorecard(models.Model):
    title = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.title

class Player(models.Model):
    name = models.CharField(max_length=10)
    score = models.IntegerField()

class PlayerForm(forms.Form):
    name = forms.CharField(max_length=10)
