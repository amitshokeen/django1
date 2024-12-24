from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30)
    selfie = models.ImageField(default='fallback.png', blank=True)

    def __str__(self):
        return self.title
