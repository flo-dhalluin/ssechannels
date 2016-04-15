from django.conf.urls import url
from .views import say_yo, event
from django.contrib.staticfiles.views import serve

urlpatterns = [
    url(r'^$', serve, kwargs={'path':'index.html'}),
    url(r'^yo/$', say_yo),
    url(r'^event/$', event),
]
