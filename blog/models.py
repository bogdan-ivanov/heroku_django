from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=500)
    body = models.TextField()
    author = models.ForeignKey(User)
    slug = models.SlugField(default='')

    def __unicode__(self):
        return self.title
