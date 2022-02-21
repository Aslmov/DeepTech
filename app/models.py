from django.db import models
from django.utils import timezone


# Create your models here.

class Message(models.Model):
    Text_chat = models.TextField()
    Text_date = models.DateTimeField(default=timezone.now())


class Challenge(models.Model):
    Theme_text = models.CharField(max_length=100)
    challenge_date = models.DateTimeField(default=timezone.now())
    nbr_participants = models.IntegerField()


class Module(models.Model):
    name_module = models.CharField(max_length=50)
    question_text = models.TextField()
    response_text = models.TextField()
    lien = models.CharField(max_length=150)