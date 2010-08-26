from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^/?$', 'blog.posts.views.index'),
    (r'^blog/$', 'blog.posts.views.blogs'),
    (r'^links/$', 'blog.posts.views.links'),
    (r'^aboutme/$', 'blog.posts.views.aboutme'),
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)
