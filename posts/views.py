from django.shortcuts import render_to_response
from blog.posts.models import Post
from django.http import HttpResponse

def index(request):
    return render_to_response('index.html',)

def blogs(request):
    latest_blogs_list = Post.objects.all().order_by('-pub_date')[:5]
    return render_to_response('posts/index.html', {'latest_blogs_list': latest_blogs_list})

def archive(request):
    latest_blogs_list = Post.objects.all().order_by('pub_date')
    return render_to_response('posts/archive.html', {'latest_blogs_list': latest_blogs_list})

def aboutme(request):
    return render_to_response('aboutme.html',)
