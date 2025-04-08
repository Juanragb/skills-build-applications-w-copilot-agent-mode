from djongo import models

class User(models.Model):
    id = models.ObjectIdField(primary_key=True, default=None)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class Team(models.Model):
    id = models.ObjectIdField(primary_key=True, default=None)
    name = models.CharField(max_length=255)
    members = models.JSONField()

class Activity(models.Model):
    id = models.ObjectIdField(primary_key=True, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    date = models.DateField()

class Leaderboard(models.Model):
    id = models.ObjectIdField(primary_key=True, default=None)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()

class Workout(models.Model):
    id = models.ObjectIdField(primary_key=True, default=None)
    name = models.CharField(max_length=255)
    description = models.TextField()
