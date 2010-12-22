from django.shortcuts import render_to_response
from blog.posts.models import Post

def index(request):
    return render_to_response('index.html',)

def ie(request):
    latest_blogs_list = Post.objects.all().order_by('pub_date')
    return render_to_response('ie.html', {'latest_blogs_list': latest_blogs_list})

def aboutme(request):
    return render_to_response('aboutme.html',)

def schedule(request):
    return render_to_response('schedule.html',)

def xmas(request):
    return render_to_response('xmas.html',)
