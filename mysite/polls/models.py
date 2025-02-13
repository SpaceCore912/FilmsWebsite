from django.db import models
from django.contrib.auth.models import User
import json
import datetime
from django.urls import reverse
import os
from uuid import uuid4
from django.utils.deconstruct import deconstructible

# Create your models here.

class Group(models.Model):
    name=models.CharField(max_length=50,blank=True)
    members= models.ManyToManyField(User)
    def __str__(self):
        return self.name
class Profile(models.Model):
    user=models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        primary_key=True)
    
    language=models.CharField(max_length=200)
    bio = models.TextField(max_length=500, blank=True)
    user_image=models.ImageField(upload_to=f'polls/static/polls/images/', blank=True)
    email=models.EmailField(max_length=70,blank=True)
    slug = models.SlugField(null=True)

    
    def get_absolute_url(self):
        return reverse("polls:profile", kwargs={"slug": self.user.username})
    def name(self):
        user=User.objects.get(username=self.user.username)
        return user.username
    def __str__(self) :
        return self.user.username

class Genre(models.Model):
    genre=models.CharField(max_length=40)
    def __str__(self):
        return self.genre



class Category(models.Model):
    name=models.CharField(max_length=40)
    def __str__(self):
        return self.name



class Film(models.Model):
    id = models.AutoField(primary_key=True)
    likes=models.IntegerField(default=0)
    description=models.CharField(default="30",max_length=500)
    name_text = models.CharField(max_length=200)
    genre=models.ManyToManyField(Genre)
    pub_date = models.IntegerField()
    director=models.CharField(max_length=200,blank=True)
 
    imageUrl=models.CharField(max_length=200,default="none")
    """@property
    def image_url(self):
        return 'polls/images/{}.jpg'.format(self.id)"""

    category=models.ManyToManyField(Category)

    def __str__(self):
        return self.name_text
    
  
class Watchlist(models.Model):
    name =models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    films=models.ManyToManyField(Film,blank=True)
    def __str__(self):
        return self.name

class Reviews(models.Model):
    text=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    film=models.ForeignKey(Film, on_delete=models.CASCADE)    
    def __str__(self):
        return self.text


class Like(models.Model):
    user=models.OneToOneField(User, on_delete=models.PROTECT)
    linked_film=models.ManyToManyField(Film,blank=True)
    
