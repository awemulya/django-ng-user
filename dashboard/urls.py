__author__ = 'awemulya'

from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns('',
                       url(r'^profile/$', views.profile, name='profile'),
                       url(r'^players/$', views.players, name='players'),
                       )