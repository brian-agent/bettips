from django.db import models
from django_countries.fields import CountryField
leagues = (
    ("premier league", "pl"),
    ("championship", 'ch'),
    ("league 1", 'lg1'),
    ("epl league 1", 'epl1'),
    ("epl league 2", 'epl2'),
    ("laliga", 'lg'),
    ("Serie A", 'sa'),
    ("Serie B", 'sb'),
    ("Bundesliga", 'bg')
)
# Create your models here.
class Fixture(models.Model):
    home_team = models.CharField(max_length=100)
    away_team = models.CharField(max_length=100)
    date = models.DateTimeField()
    created_at= models.DateTimeField(auto_now=True)
    home_team_score = models.IntegerField()
    away_team_score = models.IntegerField()
    result_home_team_score= models.IntegerField(null=True,blank=True)
    result_away_team_score= models.IntegerField(null=True,blank=True)
    league =models.CharField(choices=leagues,max_length=100)
    country = CountryField()
    season = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.home_team} vs {self.away_team} on {self.date} in {self.league} season {self.season} in {self.country}"