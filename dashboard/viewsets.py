__author__ = 'awemulya'

from.models import Players, Game
from .serializer import PlayerSerializer, GameSerializer
from rest_framework import viewsets

class PlayerViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Players.objects.all()
    serializer_class = PlayerSerializer

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