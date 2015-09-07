from rest_framework.fields import SerializerMethodField

__author__ = 'awemulya'

from rest_framework import serializers
from .models import Players, Game, Club, Fixture


class GameSerializer(serializers.ModelSerializer):
    fixtures = serializers.ReadOnlyField(source='fixture.game_fixture')
    week_score = serializers.ReadOnlyField(source='fixture.score')
    week = serializers.ReadOnlyField(source='fixture.week')
    class Meta:
        model = Game
        fields = ('id', 'points', 'fixtures', 'week','week_score')
        depth = 1
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
        }


class PlayerSerializer(serializers.ModelSerializer):
    game = GameSerializer(many=True, read_only=True)
    club_name = serializers.ReadOnlyField(source="club.name", read_only=True)
    club = serializers.PrimaryKeyRelatedField(queryset=Club.objects.all())
    game_point = serializers.IntegerField(source='point', read_only=True)
    total_points = serializers.IntegerField(source='points', read_only=True)
    player_age = serializers.IntegerField(source='age', read_only=True)

    class Meta:
        model = Players
        fields = ('id', 'name', 'position', 'date_of_birth', 'game', 'club', 'club_name', 'game_point', 'total_points', 'player_age')
        depth = 2
        extra_kwargs = {
        "id": {
            "read_only": False,
            "required": False,
        },
        }


class FixtureSerializer(serializers.ModelSerializer):
    home = serializers.PrimaryKeyRelatedField(queryset=Club.objects.all())
    away = serializers.PrimaryKeyRelatedField(queryset=Club.objects.all())
    game_fixture_text = serializers.CharField(source='game_fixture', read_only=True)
    score_text = serializers.CharField(source='score', read_only=True)
    class Meta:
        model = Fixture
        fields = ('id', 'week', 'home', 'away', 'home_goals', 'away_goals', 'time','played',
                  'score_text', 'game_fixture_text')
        depth = 1
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
        }


class ClubSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many=True, read_only=True)
    game = SerializerMethodField('get_games', read_only= True)

    class Meta:
        model = Club
        fields = ('id', 'name', 'established', 'players', 'game')
        depth = 3

        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
        }

    def get_games(self, club):
        from django.db.models import Q
        fixtures = Fixture.objects.filter(Q(home=club) | Q(away=club))
        serializer = FixtureSerializer(instance=fixtures, many=True)
        return serializer.data

