# Server Sent Events for django/channels

This module enable the use of SSE with [channels](https://https://github.com/andrewgodwin/channels).
*This module has only been tested with python3.4 *

## Server side how to :

This modules (as SSEs in my opinion) is build around the idea of publish/suscribe architecture.
SSE endpoints in your django applications are regular views, but decorated with the sse.subscriber.

If the decorated view returns anything else than an HttpResponse object :
- a channel Group is created with the supplied name
- headers are set to SSE headers
- the connection is left open

```python
from ssechannels import sse

@sse.subscribe("yo") # creates a "yo" Group for sending events
def yo_events(rq) :
    pass
```

You are not forced to hard code a specific group name, in that case, you have to return the group name as a string object. You can send regular responses  for example :

```python
@sse.subscribe() # not specifying a channel name
def yo_for_user_events(rq):
    if(not rq.user.is_authenticated()):
        return HttpResponseForbidden("Please login")

    return "yo.%s"%rq.user.username # returns channel name
```

These views, can be routed the usual django urls way. (no need to specify channels consumers and all ! )


You can now send events to listeners (for example in a signal here ... ) with :

```python
from ssechannels import sse


@receiver(post_save, sender=Yo)
def send_sse(sender, instance, **kwargs):
	sse.publish("yo", # <- sse group name
                b"yo", # <- event 
                "yo from %s to %s"%(instance.from_user,
                                    instance.to_user))

```

## Client side

[A good ref on SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events)

```javascript

var sse = new EventSource("events/yo");
var eventbox = document.querySelector("#yo");
  
sse.addEventListener("yo", function(e) {

	var el = document.createElement('p');
	el.innerHTML = e.data;
    console.log(e.data);

    eventbox.appendChild(el);
});

```

see also the demo project in this repos.

