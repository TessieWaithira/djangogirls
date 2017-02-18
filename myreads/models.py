from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


# Create your models here.
# title
# text summary
# date
# user
class Test(models.Model):
    title = models.CharField(max_length=100)


class Gist(models.Model):
    user = models.ForeignKey('auth.User')
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
