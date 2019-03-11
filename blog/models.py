from __future__ import unicode_literals

from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=16, default='title')
    content = models.TextField(null=True)
    def __unicode__(self):
        return self.title
class User(models.Model):
    username = models.IntegerField(max_length= 11,primary_key=True)
    password =models.CharField(max_length=16)