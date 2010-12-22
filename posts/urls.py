from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('blog.posts.views',
    (r'^$', 'index'),
    (r'^archive/$', 'archive'),
)
