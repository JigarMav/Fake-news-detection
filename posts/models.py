from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title = models.TextField()
    content = models.TextField()
    image = models.ImageField()
    publisher = models.TextField(max_length=260)
    source = models.TextField()
    votes = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __init__(self):
        return self.title

    def get_votes(self):
        self.votes = self.votes+1
        return self.votes






