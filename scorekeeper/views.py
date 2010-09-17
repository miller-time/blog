from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from blog.scorekeeper.models import Scorecard, PlayerForm, Player, UpdateForm
from django.forms.formsets import formset_factory

def index(request):
    players = Player.objects.all()
    if request.method == "POST": # if form has been submitted
        addplayer = PlayerForm(request.POST) # form bound to POST data
        if addplayer.is_valid(): # passes all validation rules
            fname = addplayer.cleaned_data['name']
            p = Player(name=fname, score=0)
            p.save()
            return HttpResponseRedirect('/scorekeeper/') # redirect after POST
    else:
        addplayer = PlayerForm() # unbound form

    return render_to_response('scorekeeper/index.html', {
        'addplayer': addplayer,
        'players': players,
    }, context_instance=RequestContext(request))

def play(request):
    players = Player.objects.all()
    num_p = len(players)
    UpdateFormSet = formset_factory(UpdateForm, extra=num_p-1)
    if request.method == "POST":
        formset = UpdateFormSet(initial=[{'score': 0}])
        if formset.is_valid():
            i = 0
            for form in formset.forms:
                points = form.cleaned_data['score']
                players[i].score += points
                players[i].save()
                i += 1
            return HttpResponseRedirect('/scorekeeper/play')
    else:
        formset = UpdateFormSet(initial=[{'score': 0}])

    return render_to_response('scorekeeper/play.html', {
        'formset': formset,
        'players': players,
    }, context_instance=RequestContext(request))
    
def end(request):
    players = Player.objects.all()
    # find winner..
    for p in players:
        p.delete()
    return render_to_response('scorekeeper/end.html')
