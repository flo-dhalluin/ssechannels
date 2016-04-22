from django.http import HttpResponse
from channels import Group
from channels.handler import AsgiRequest

def publish(group_name, event, data):
    # todo : buffer StringIO style  
    msg = b'event:' + event + b'\n'
    msg += b'data:' + data.encode() + b'\n\n'
    Group(group_name).send({
        "content": msg,
        "more_content": True,
    })


# them subscribe decorator
class subscribe(object):
    
    def __init__(self, group_name=None) :
        self.group_name = group_name


    def __call__(self, view) :
        def wrapped(req, *args, **kwargs) :
            r = view(req, *args, **kwargs)

            if(isinstance(r, HttpResponse)) :
                return r

            reply = {
                'status': 200,
                'headers': [('Content-Type','text/event-stream'),], # we shall probably setup cache headers right as well
                'more_content': True
            }
        
            if(r) :
                group_name = r
            else : 
                group_name = self.group_name

            req.message.reply_channel.send(reply)
            Group(group_name).add(req.message.reply_channel)

            # pop !
            raise AsgiRequest.ResponseLater()


        return wrapped
