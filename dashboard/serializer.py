__author__ = 'awemulya'

from rest_framework import serializers
from .models import Players, Game


class GameSerializer(serializers.HyperlinkedModelSerializer):
    # player = serializers.HyperlinkedRelatedField(many=False, view_name='players-detail', read_only=True)

    class Meta:
        model = Game
        fields = ('url', 'week', 'player')


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    game = serializers.HyperlinkedRelatedField(many=True, view_name='game-detail', read_only=True)
    game_point = serializers.IntegerField(source='point', read_only=True)
    total_points = serializers.IntegerField(source='points', read_only=True)

    class Meta:
        model = Players
        fields = ('url', 'name', 'position', 'game', 'club', 'game_point', 'total_points')