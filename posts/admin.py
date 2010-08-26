from blog.posts.models import Post
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
    fields = ['title','author','body']
    list_display = ['title','pub_date','up_date']
    list_filter = ['pub_date']
    search_fields = ['question']
    date_hierarchy = 'pub_date'

admin.site.register(Post, PostAdmin) 
