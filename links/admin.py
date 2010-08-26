from blog.links.models import Link
from django.contrib import admin

class LinkAdmin(admin.ModelAdmin):
    fields = ['title','location']
    list_display = ['title','location']

admin.site.register(Link, LinkAdmin)
