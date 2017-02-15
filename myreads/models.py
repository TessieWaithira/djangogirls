from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


# Create your models here.
# title
# text summary
# date
# user

class Gist(models.Model):
    user = models.ForeignKey('auth.User')
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
