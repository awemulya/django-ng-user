__author__ = 'awemulya'

from rest_framework import serializers
from .models import Players, Game, Club, Fixture


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ('id', 'name', 'established')
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
        }


class FixtureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fixture
        fields = ('id', 'week', 'home', 'away', 'home_score', 'away_score', 'time')
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
        }

class GameSerializer(serializers.ModelSerializer):
    fixture = FixtureSerializer(many=True)
    class Meta:
        model = Game
        fields = ('id', 'points', 'fixture')
        depth = 1
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
        }


class PlayerSerializer(serializers.ModelSerializer):
    game = GameSerializer(many=True)
    club = serializers.ReadOnlyField(source="club.name", read_only=True)
    game_point = serializers.IntegerField(source='point', read_only=True)
    total_points = serializers.IntegerField(source='points', read_only=True)
    player_age = serializers.IntegerField(source='age', read_only=True)

    class Meta:
        model = Players
        fields = ('id', 'name', 'position', 'game', 'club', 'game_point', 'total_points', 'player_age')
        depth = 2
        extra_kwargs = {
        "id": {
            "read_only": False,
            "required": False,
        },
        }


