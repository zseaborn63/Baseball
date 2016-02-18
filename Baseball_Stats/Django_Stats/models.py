from django.db import models

# Create your models here.


class Player(models.Model):
    lahmanID = models.IntegerField()
    player_key = models.CharField(max_length=10)
    managerID = models.CharField(max_length=10, blank=True)
    hofID = models.CharField(max_length=10, blank=True)
    birthYear = models.IntegerField()
    birthMonth = models.IntegerField()
    birthDay = models.IntegerField()
    birthCountry = models.CharField(max_length = 50)
    birthState = models.CharField(max_length = 2, blank=True)
    birthCity = models.CharField(max_length = 50)
    deathYear = models.IntegerField(blank=True)
    deathMonth = models.IntegerField(blank=True)
    deathDay = models.IntegerField(blank=True)
    deathCountry = models.CharField(max_length = 50, blank=True)
    deathState = models.CharField(max_length = 2, blank=True)
    deathCity = models.CharField(max_length = 50, blank=True)
    nameFirst = models.CharField(max_length=50)
    nameLast = models.CharField(max_length=50)
    nameNote = models.CharField(max_length=255)
    nameGiven = models.CharField(max_length=255)
    nameNick = models.CharField(max_length=255)
    height = models.IntegerField()
    weight = models.IntegerField()
    bats = models.CharField(max_length=1, choices=(('L', 'Left'), ('R', 'Right'), ('B', 'Both')))
    throws = models.CharField(max_length=1, choices=(('L', 'Left'), ('R', 'Right'), ('B', 'Both')))
    debut = models.CharField(max_length=12)
    finalGame = models.CharField(max_length=12, blank=True)
    college = models.CharField(max_length=50, blank=True)
    lahman40ID = models.CharField(max_length=9)
    lahman45ID = models.CharField(max_length=9)
    holtzID = models.CharField(max_length=9)
    bbrefID = models.CharField(max_length=9)

    
