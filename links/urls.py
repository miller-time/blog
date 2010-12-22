from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('blog.links.views',
    (r'^$', 'index'),
)
