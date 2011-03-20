from django.db import models
from django.contrib.auth.models import User
from django.contrib.syndication.views import Feed

class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts')
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    up_date = models.DateTimeField('last modified', auto_now=True)
    
    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "http://millertime.dnsdojo.com/blog/"

class BlogFeed(Feed):
    title = "Millertime Blog"
    link = "/blog/"
    description = "Latest entries from my blog."

    def items(self):
        return Post.objects.all().order_by('-pub_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body
