from slideshow.models import Slide
from django.contrib import admin

class SlideAdmin(admin.ModelAdmin):
    filename = 'filename'
    date_added = 'date_added'

admin.site.register(Slide, SlideAdmin) 
