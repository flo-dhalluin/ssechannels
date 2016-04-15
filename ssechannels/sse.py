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
    
    def __init__(self, group_name) :
        self.group_name = group_name


    def __call__(self, view) :
        def wrapped(req) :

            reply = {
                'status': 200,
                'headers': [('Content-Type','text/event-stream'),], # we shall probably setup cache headers right as well
                'more_content': True
            }
        
        
            req.message.reply_channel.send(reply)
            Group(self.group_name).add(req.message.reply_channel)

            # pop !
            raise AsgiRequest.ResponseLater()


        return wrapped
