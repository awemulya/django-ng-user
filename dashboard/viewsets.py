__author__ = 'awemulya'

from.models import Players, Game, Club, Fixture
from .serializer import PlayerSerializer, GameSerializer, ClubSerializer, FixtureSerializer
from rest_framework import viewsets

class PlayerViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Players.objects.all()
    serializer_class = PlayerSerializer

    def perform_create(self, serializer):
            serializer.save()


class FixtureViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Fixture.objects.all()
    serializer_class = FixtureSerializer

    def perform_create(self, serializer):
            serializer.save()


class GameViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def perform_create(self, serializer):
            serializer.save()


class ClubViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

    def perform_create(self, serializer):
            serializer.save()