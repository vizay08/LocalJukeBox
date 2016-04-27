from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=750)
    author = models.CharField(max_length=750)
    counter = models.IntegerField(default=1)
    token = models.CharField(max_length=6,default='adad')
    coverimage_location = models.CharField(max_length=1000)
    song_directory = models.TextField()
    is_playing = models.BooleanField(default=False)

    def __str__(self):
        return self.title


