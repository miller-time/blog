from slideshow.models import Slide
from django.contrib import admin

class SlideAdmin(admin.ModelAdmin):
    filename = 'filename'

admin.site.register(Slide, SlideAdmin) 
