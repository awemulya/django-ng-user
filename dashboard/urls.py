__author__ = 'awemulya'

from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter
from . import views
from .viewsets import PlayerViewSet, GameViewSet, ClubViewSet

router = DefaultRouter()
router.register(r'players', PlayerViewSet)
router.register(r'games', GameViewSet)
router.register(r'clubs', ClubViewSet)


urlpatterns = patterns('',
                       url(r'^', include(router.urls)),
                       url(r'^dashboard/$', views.dashboard, name='dashboard'),
                       url(r'^players/$', views.players, name='players'),
                       )