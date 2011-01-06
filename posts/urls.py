from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('blog.posts.views',
    (r'^$', 'index'),
    (r'^archive/$', 'archive'),
    (r'^archive/jun2010/$', 'archive_jun2010'),
    (r'^archive/jul2010/$', 'archive_jul2010'),
    (r'^archive/aug2010/$', 'archive_aug2010'),
    (r'^archive/sep2010/$', 'archive_sep2010'),
    (r'^archive/oct2010/$', 'archive_oct2010'),
    (r'^archive/nov2010/$', 'archive_nov2010'),
    (r'^archive/dec2010/$', 'archive_dec2010'),
    (r'^archive/jan2011/$', 'archive_jan2011'),
)
