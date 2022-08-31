from django.db import models

# Create your models here.


class Team(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=120)
    division=models.CharField(max_length=100)
    number_of_wins=models.PositiveIntegerField()
    number_of_losses=models.PositiveIntegerField()

    def __str__(self):
            return self.name

class Players(models.Model):
    team=models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
    name=models.CharField(max_length=100)
    position=models.CharField(max_length=100)
    age=models.IntegerField()
    injured_reserved_list=models.BooleanField()

    def __str__(self):
        return self.name

class Conference(models.Model):
    team=models.ForeignKey(Team, on_delete=models.CASCADE, related_name='conference')
    conference=models.CharField(max_length=100)
    

    def __str__(self):
         return self.conference