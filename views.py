from django.shortcuts import render_to_response
from blog.posts.models import Post
from blog.slideshow.models import Slide
from django.views.generic import TemplateView

def ie(request):
    latest_blogs_list = Post.objects.all().order_by('pub_date')
    return render_to_response('ie.html', {'latest_blogs_list': latest_blogs_list})

def pics(request):
    all_slides = Slide.objects.all().order_by('-date_added')
    newest = all_slides[0]
    old_slides = all_slides[1:]
    return render_to_response('pics.html', {'newest':newest, 'old_slides':old_slides})

def schedule(request):
    return render_to_response('schedule.html',)

def downloads(request):
    return render_to_response('downloads.html',)

def random(request):
    return render_to_response('random.html',)

# test views for error pages
def test500(request):
    return render_to_response('500.html',)

def test404(request):
    return render_to_response('404.html',)

