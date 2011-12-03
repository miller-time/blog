from django.shortcuts import render_to_response
from blog.posts.models import Post
from blog.slideshow.models import Slide

def ie(request):
    latest_blogs_list = Post.objects.all().order_by('pub_date')
    return render_to_response('ie.html', {'latest_blogs_list': latest_blogs_list})

def pics(request):
    all_slides = Slide.objects.all().order_by('-date_added')
    newest = all_slides[0]
    old_slides = all_slides[1:]
    return render_to_response('pics.html', {'newest':newest, 'old_slides':old_slides})
