from django.shortcuts import render
from django.http import HttpResponse
from channels import Group

from ssechannels import sse

# that's an event source, note the raise at the end : 
# this tells channels view processor to fuck off. 

# use cases -> subscribe --> add reply_channel to some named group

# user-level event 
# (think async messaging "you've got mail")
# store the reply_channel id in some user/session attached storage (short term) ? 

@sse.subscribe("yo")
def event(rq) :
    pass
    # or -- return sse.SubscribeResponse("yo") ??

def say_yo(rq):
    # this gets sent to all subscribers
    sse.publish("yo", b"yo", "this is yo speaking");
    return HttpResponse("Ok")
