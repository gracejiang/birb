from django.db import models

# modifying this file --> need to make a migration

class Chirp(models.Model):
    body = models.TextField(max_length=300)

    def __str__(self):
        return self.body