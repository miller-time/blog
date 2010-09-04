from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^/?$', 'blog.posts.views.index'),
    (r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/media/favicon.ico'}),
    (r'^blog/$', 'blog.posts.views.blogs'),
    (r'^archive/$', 'blog.posts.views.archive'),
    (r'^links/$', 'blog.links.views.index'),
    (r'^aboutme/$', 'blog.posts.views.aboutme'),
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)
