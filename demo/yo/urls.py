from django.conf.urls import url
from .views import say_yo, yo_events, yo_for_user_events
from django.contrib.staticfiles.views import serve

urlpatterns = [
    url(r'^$', serve, kwargs={'path':'index.html'}),
    url(r'^yo/(?P<username>\w+)$', say_yo),
    url(r'^all_yos/$', yo_events),
    url(r'^my_yos/$', yo_for_user_events),

]
