from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('blog.views',
    (r'^/?$', 'index'),
    (r'^ie/$', 'ie'),
    (r'^aboutme/$', 'aboutme'),
    (r'^schedule/$', 'schedule'),
    (r'^xmas/$', 'xmas'),
)

urlpatterns += patterns('',
    (r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/media/favicon.ico'}),
    (r'^admin/', include(admin.site.urls)),
    (r'^blog/', include('posts.urls')),
    (r'^links/', include('links.urls')),
    (r'^photo/', include('photo.urls')),
)
