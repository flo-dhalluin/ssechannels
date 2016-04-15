from django.http import HttpResponse

from channels.handler import AsgiHandler, ViewConsumer
from channels import Group


default_consumer = ViewConsumer()

def http_consumer(msg) :
    # hijack if path matches
    path = msg['path']
    if(path.strip(b'/') == b'event'):
        r = HttpResponse("Well")

        # open up SSE stream
        reply = {
            'status': 200,
            'headers': [('Content-Type','text/event-stream'),], # we shall probably setup cache headers right as well
            'more_content': True
        }
        print("event subscriptions", msg.reply_channel)
        msg.reply_channel.send(reply)
        Group('yo').add(msg.reply_channel)
        # the problem being there's not 
        # disconnect event with SSE, nor with channels 
        # the only way to get this is erroring on sending 
        # data ..

    else :
        # handover to django's wsgi 
        default_consumer(msg)
