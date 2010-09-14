from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from blog.scorekeeper.models import Scorecard, PlayerForm

def index(request):
    score_card = Scorecard.objects.all()
    return render_to_response('scorekeeper/index.html', {
        'score_card': score_card
    })

def players(request):
    if request.method == "POST": # if form has been submitted
        form = PlayerForm(request.POST) # form bound to POST data
        if form.is_valid(): # passes all validation rules
            # process data
            return HttpResponseRedirect('/scorekeeper/') # redirect after POST
    else:
        form = PlayerForm() # unbound form

    return render_to_response('scorekeeper/players.html', {
        'form': form,
    }, context_instance=RequestContext(request))
