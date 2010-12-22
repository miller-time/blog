from django.conf.urls.defaults import *
from blog.photo.models import *

urlpatterns = patterns('blog.photo.views',
   (r"^(\d+)/$", "album"),
   (r"^(\d+)/(full|thumbnails|edit)/$", "album"),
   (r"^update/$", "update"),
   (r"^search/$", "search"),
   (r"^image/(\d+)/$", "image"),
   (r"", "main"),
)
