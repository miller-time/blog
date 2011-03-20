from django.shortcuts import render_to_response
from blog.posts.models import Post

def index(request):
    latest_blogs_list = Post.objects.all().order_by('-pub_date')[:5]
    return render_to_response('posts/index.html', {'latest_blogs_list': latest_blogs_list})

def archive(request):
    return render_to_response('posts/archive.html', )

def archive_jun2010(request):
    jun2010 = Post.objects.filter(pub_date__year=2010, pub_date__month=6)
    return render_to_response('posts/jun2010.html', {'jun2010': jun2010})

def archive_jul2010(request):
    jul2010 = Post.objects.filter(pub_date__year=2010, pub_date__month=7)
    return render_to_response('posts/jul2010.html', {'jul2010': jul2010})

def archive_aug2010(request):
    aug2010 = Post.objects.filter(pub_date__year=2010, pub_date__month=8)
    return render_to_response('posts/aug2010.html', {'aug2010': aug2010})

def archive_sep2010(request):
    sep2010 = Post.objects.filter(pub_date__year=2010, pub_date__month=9)
    return render_to_response('posts/sep2010.html', {'sep2010': sep2010})

def archive_oct2010(request):
    oct2010 = Post.objects.filter(pub_date__year=2010, pub_date__month=10)
    return render_to_response('posts/oct2010.html', {'oct2010': oct2010})

def archive_nov2010(request):
    nov2010 = Post.objects.filter(pub_date__year=2010, pub_date__month=11)
    return render_to_response('posts/nov2010.html', {'nov2010': nov2010})

def archive_dec2010(request):
    dec2010 = Post.objects.filter(pub_date__year=2010, pub_date__month=12)
    return render_to_response('posts/dec2010.html', {'dec2010': dec2010})

def archive_jan2011(request):
    jan2011 = Post.objects.filter(pub_date__year=2011, pub_date__month=1)
    return render_to_response('posts/jan2011.html', {'jan2011': jan2011})

def archive_feb2011(request):
    feb2011 = Post.objects.filter(pub_date__year=2011, pub_date__month=2)
    return render_to_response('posts/feb2011.html', {'feb2011': feb2011})

def archive_mar2011(request):
    mar2011 = Post.objects.filter(pub_date__year=2011, pub_date__month=3)
    return render_to_response('posts/mar2011.html', {'mar2011': mar2011})
