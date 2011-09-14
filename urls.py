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

urlpatterns += patterns(
    '',
    (r'^favicon\.ico$', redirect_to, {'url': '/media/favicon.ico'}),
    (r'^admin/', include(admin.site.urls)),
    (r'^blog/', include('posts.urls')),
    (r'^links/', include('links.urls')),
)
