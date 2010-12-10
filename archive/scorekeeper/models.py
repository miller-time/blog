from django.db import models
from django import forms
from django.forms import ModelForm


class Player(models.Model):
    name = models.CharField(max_length=10)
    score = models.IntegerField()

class PlayerForm(ModelForm):
    class Meta:
        model = Player

class UpdateForm(ModelForm):
    class Meta:
        model = Player
        fields = ('score',)
