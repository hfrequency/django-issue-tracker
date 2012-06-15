from django.db import models
from django.contrib.auth.models import User

class Comments(models.Model):
    comment = models.CharField(max_length=500)
    user = models.ForeignKey(User)

class Level(models.Model):
    level_choices = (
        (0, "LOW"),
        (1, "MEDIUM"),
        (2, "HIGH"),
        (3, "CRITICAL"),
        (4, "BLOCKER"),
    )
    level = models.CharField(max_length=10, choices=level_choices)

class Status(models.Model):
    status_choices = (
        (0, "OPEN"),
        (1, "IN PROGRESS"),
        (2, "FINISHED"),
        (3, "CLOSED"),
        (4, "CANCELED"),
    )
    status = models.CharField(max_length=10, choices=status_choices)

class Issue(models.Model):
    status = models.ForeignKey(Status)
    level = models.ForeignKey(Level)
    comments = models.ForeignKey(Comments, null=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    priority = models.CharField(max_length=10)  
    date_created = models.DateField() 
    date_completed = models.DateField() 
    # TODO implement these
    # time_estimate 
    # percentage_completed  

class Project(models.Model):
    user = models.ForeignKey(User)
    issue = models.ForeignKey(Issue, null=True)
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=15, null=True)
    release_date = models.DateField(null=True)

