from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from blog.scorekeeper.models import PlayerForm, Player, UpdateForm
from django.forms.models import modelformset_factory

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
    UpdateFormSet = modelformset_factory(UpdateForm)
    if request.method == "POST":
        formset = UpdateFormSet(request.POST)
        if formset.is_valid():
            i = 0
            for form in formset.forms:
                Player.objects.filter(pk=player.pk).update(score=F('score')+points)
            return HttpResponseRedirect('/scorekeeper/play')
    else:
        formset = UpdateFormSet()

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
