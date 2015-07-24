from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User


class Card(models.Model):

    owner = models.ForeignKey(User)
    url = models.URLField()
    nume = models.CharField(max_length=60)
    image = models.ImageField()
    media_type = models.CharField(max_length=32)
    created_at = models.DateTimeField('date created')

    def __str__(self):
        return self.nume

    
