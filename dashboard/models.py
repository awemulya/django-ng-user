import datetime
from django.db import models
from django.db.models import Q


class Club(models.Model):
    name = models.CharField(max_length=30, default='Manchester City')
    established = models.DateField(null=True)

    def league_points(self):
        fixtures = Fixture.objects.filter(Q(home=self) | Q(away=self) & Q(played=True))
        points = 0;
        for fix in fixtures:
            if fix.home == self:
                if fix.home_goals == fix.away_goals:
                    points += 1
                elif fix.home_goals > fix.away_goals:
                    points += 3
            else:
                if fix.home_goals == fix.away_goals:
                    points +=1
                elif fix.away_goals > fix.home_goals:
                    points += 3
        return points

class Players(models.Model):
    POSITION_CHOICES = (
        ('forward', 'Forward'),
        ('midfielder', 'Midfielder'),
        ('defender', 'Defender'),
        ('goalkeeper', 'GoalKeeper'),
    )
    name = models.CharField(max_length=255, verbose_name="name", db_index=True)
    date_of_birth = models.DateField()
    position = models.CharField(max_length=12, choices=POSITION_CHOICES, default='forward')
    club = models.ForeignKey(Club, null=True, related_name="players")

    def __unicode__(self):
        return u'%s' % (self.name)

    def age(self):
        return int((datetime.date.today() - self.date_of_birth).days / 365.25)

    def point(self):
        if not self.game.all().count():
            return 0
        return self.game.all().order_by('-id')[0].points

    def points(self):
        if not self.game.all().count():
            return 0
        games = self.game.all()
        point = 0
        for game in games:
            point += game.points
        return point


class Fixture(models.Model):
    home = models.ForeignKey(Club, related_name="home")
    away = models.ForeignKey(Club, related_name="away")
    week = models.IntegerField(default=0)
    home_goals = models.IntegerField(default=0)
    away_goals = models.IntegerField(default=0)
    time = models.DateTimeField(null=True)
    played = models.BooleanField(default=False)

    def game_fixture(self):
        return self.home.name+' vs ' + self.away.name

    def score(self):
        return str(self.home_goals)+' - ' + str(self.away_goals)


class Game(models.Model):
    points = models.IntegerField(default=0)
    player = models.ForeignKey(Players, related_name='game')
    fixture = models.ForeignKey(Fixture, related_name="fixture")

    def __unicode__(self):
        return  u'%s, %s, %s' % (self.player,self.week,self.points)