from django.shortcuts import render_to_response
from blog.posts.models import Post

def index(request):
    latest_blogs_list = Post.objects.all().order_by('-pub_date')[:5]
    return render_to_response('posts/index.html', {'latest_blogs_list': latest_blogs_list})

def archive(request):
    latest_blogs_list = Post.objects.all().order_by('pub_date')
    return render_to_response('posts/archive.html', {'latest_blogs_list': latest_blogs_list})
