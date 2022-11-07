from turtle import title
from django.db import models

# Create your models here.

class Article(models.Model):
    image = models.ImageField(upload_to='img')
    title = models.CharField(max_length = 60)
    summary = models.CharField(max_length = 100)
    post_slug = models.SlugField(null=True, max_length = 200)
    author = models.CharField(max_length = 20)
    date = models.DateField()
    content = models.TextField(max_length = 10000)

class Message(models.Model):
    name = models.CharField(max_length = 20)
    email = models.EmailField()
    phone = models.CharField(max_length = 10)
    message = models.TextField(max_length = 1000)