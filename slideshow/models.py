from django.db import models

class Slide(models.Model):
    filename = models.CharField(max_length=200)

    def __unicode__(self):
        return self.filename
