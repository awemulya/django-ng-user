__author__ = 'awemulya'

from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from . import views
from .viewsets import PlayerViewSet, GameViewSet

router = DefaultRouter()
router.register(r'players', PlayerViewSet)
router.register(r'games', GameViewSet)


urlpatterns = patterns('',
                       url(r'^', include(router.urls)),
                       url(r'^home/$', views.home, name='home'),
                       url(r'^players/$', views.players, name='players'),
                       )