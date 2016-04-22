from django.db import models
from django.contrib.auth.models import User

class Yo(models.Model):
    date_sent = models.DateTimeField(auto_now_add=True)
    from_user = models.ForeignKey(User, related_name='+')
    to_user = models.ForeignKey(User, related_name='+')
