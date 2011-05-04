from django.conf.urls.defaults import *
from blog.posts.models import BlogFeed

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('blog.posts.views',
    (r'^$', 'index'),
    (r'^feed/$', BlogFeed()),
    (r'^archive/$', 'archive'),
    (r'^archive/jun2010/$', 'archive_jun2010'),
    (r'^archive/jul2010/$', 'archive_jul2010'),
    (r'^archive/aug2010/$', 'archive_aug2010'),
    (r'^archive/sep2010/$', 'archive_sep2010'),
    (r'^archive/oct2010/$', 'archive_oct2010'),
    (r'^archive/nov2010/$', 'archive_nov2010'),
    (r'^archive/dec2010/$', 'archive_dec2010'),
    (r'^archive/jan2011/$', 'archive_jan2011'),
    (r'^archive/feb2011/$', 'archive_feb2011'),
    (r'^archive/mar2011/$', 'archive_mar2011'),
    (r'^archive/apr2011/$', 'archive_apr2011'),
    (r'^archive/may2011/$', 'archive_may2011'),
)
