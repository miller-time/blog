from django.db import models

class Slide(models.Model):
    filename = models.CharField(max_length=200)
    date_added = models.DateTimeField('date_added', auto_now_add=True)

    def __unicode__(self):
        return self.filename
