import datetime
from django.db import models


class Club(models.Model):
    name = models.CharField(max_length=30, default='Manchester City')
    established = models.DateField(null=True)

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
        return self.game.all().order_by('week')[0].points

    def points(self):
        if not self.game.all().count():
            return 0
        games = self.game.all()
        point = 0
        for game in games:
            point += game.points
        return point

class Game(models.Model):
    week = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    player = models.ForeignKey(Players, related_name='game')
    fixture = models.CharField(max_length=50, null=True)

    def __unicode__(self):
        return  u'%s, %s, %s' % (self.player,self.week,self.points)