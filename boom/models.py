from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Song(models.Model):
    movie=models.CharField(max_length=200,blank=True)
    song_name=models.CharField(max_length=200)
    artist=models.CharField(max_length=200)
    year=models.IntegerField()
    image=models.ImageField(upload_to='images/')
    song_file=models.FileField(upload_to='songs/')



    def __str__(self):
        return self.song_name

class Playlist(models.Model):
    list_name=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    song=models.ManyToManyField(Song, blank=True)

    def __str__(self):
        return self.list_name

class Favourite(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    song=models.ForeignKey(Song,on_delete=models.CASCADE, blank=True,null=True)

    def __str__(self):
        return self.user


class Recent(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    song=models.ForeignKey(Song,on_delete=models.CASCADE, blank=True,null=True)
