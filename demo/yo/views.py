from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required

from .models import Yo
from django.contrib.auth.models import User

from ssechannels import sse

@sse.subscribe("allyo")
def yo_events(rq) :
    pass
    # or -- return sse.SubscribeResponse("yo") ??

@sse.subscribe() # not specifying a channel name
def yo_for_user_events(rq):
    if(not rq.user.is_authenticated()):
        return HttpResponseForbidden("Please login")

    return "yo.%s"%rq.user.username # returns channel name


@login_required
def say_yo(rq, username):
    to_user = get_object_or_404(User, username=username)
    # this gets sent to all subscribers
    yo = Yo.objects.create(from_user=rq.user, 
                           to_user=to_user)
    return HttpResponse("Ok")
