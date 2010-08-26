from django.shortcuts import render_to_response
from blog.links.models import Link

def index(request):
    links_list = Link.objects.all()
    return render_to_response('links/index.html', {'links_list': links_list})
