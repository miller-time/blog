import settings
from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    'blog.views',
    (r'^/?$', redirect_to, {'url': '/blog/'}),
    (r'^ie/$', 'ie'),
    (r'^aboutme/$', TemplateView.as_view(template_name='aboutme.html')),
    (r'^pics/$', 'pics'),
    (r'^schedule/$', TemplateView.as_view(template_name='schedule.html')),
    (r'^downloads/$', TemplateView.as_view(template_name='downloads.html')),
    (r'^random/$', TemplateView.as_view(template_name='random.html')),
)

# this TOTALLY works! It shows the actual 404/500 pages 
# instead of the debug trace. 
# Just go to url.com/404/ or url.com/500/ to see.
if settings.DEBUG:
    urlpatterns += patterns('blog.views',
        (r'^500/', TemplateView.as_view(template_name='500.html')),
        (r'^404/', TemplateView.as_view(template_name='404.html')),
    )

urlpatterns += patterns('',
    (r'^favicon\.ico$', redirect_to, {'url': '/media/favicon.ico'}),
    (r'^admin/', include(admin.site.urls)),
    (r'^blog/', include('posts.urls')),
    (r'^links/', include('links.urls')),
)
