from django.db import models
from django.contrib.auth.models import User

# modifying this file --> need to make a migration

class Hashtag(models.Model):
    tag = models.CharField(max_length=30)
    
    def __str__(self):
        return self.tag

class Chirp(models.Model):
    body = models.TextField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now=True)

    # foreign keys link one model to another
    hashtags = models.ManyToManyField(Hashtag)

    def __str__(self):
        return self.body