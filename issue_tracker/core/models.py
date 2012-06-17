from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    user = models.ForeignKey(User)
    # issue = models.ForeignKey(Issue, null=True)
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=15, null=True)
    release_date = models.DateField(null=True)

class Issue(models.Model):
    project = models.ForeignKey(Project)
    status_choices = (
        ("0", "OPEN"),
        ("1", "IN PROGRESS"),
        ("2", "FINISHED"),
        ("3", "CLOSED"),
        ("4", "CANCELED"),
    )
    status = models.CharField(max_length=10, choices=status_choices)
    level_choices = (
        ("0", "LOW"),
        ("1", "MEDIUM"),
        ("2", "HIGH"),
        ("3", "CRITICAL"),
        ("4", "BLOCKER"),
    )
    level = models.CharField(max_length=10, choices=level_choices)
    comments = models.ForeignKey(Comments, null=True)
    title = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=50, null=True)
    date_created = models.DateField(auto_now_add=True) 
    date_completed = models.DateField(null=True) 
    # TODO implement these
    # time_estimate 
    # percentage_completed  

class Comments(models.Model):
    issue = models.ForeignKey(Issue)
    comment = models.CharField(max_length=500)
    user = models.ForeignKey(User)

