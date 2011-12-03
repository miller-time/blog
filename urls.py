import settings
from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    'blog.views',
    (r'^/?$', redirect_to, {'url': '/blog/'}),
    (r'^ie/$', 'ie'),
    (r'^aboutme/$', 'aboutme'),
    (r'^pics/$', 'pics'),
    (r'^schedule/$', 'schedule'),
    (r'^downloads/$', 'downloads'),
    (r'^random/$', 'random'),                   
)

# this TOTALLY works! It shows the actual 404/500 pages 
# instead of the debug trace. 
# Just go to url.com/404/ or url.com/500/ to see.
if settings.DEBUG:
    urlpatterns += patterns('blog.views',
        (r'^500/', 'test500'),
        (r'^404/', 'test404'),
    )

urlpatterns += patterns('',
    (r'^favicon\.ico$', redirect_to, {'url': '/media/favicon.ico'}),
    (r'^admin/', include(admin.site.urls)),
    (r'^blog/', include('posts.urls')),
    (r'^links/', include('links.urls')),
)
