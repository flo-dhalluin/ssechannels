from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Yo
from ssechannels import sse


@receiver(post_save, sender=Yo)
def my_handler(sender, instance, **kwargs):
    print("sending some yos over")
    sse.publish("allyo", # <- sse group name
                b"yo", # <- event 
                "yo from %s to %s"%(instance.from_user,
                                    instance.to_user))

    sse.publish("yo.%s"%instance.to_user.username,
                b"yo",
                "got a yo from %s"%instance.from_user)
