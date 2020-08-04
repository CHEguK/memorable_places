''' memories/models.py '''
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class MemoryItem(models.Model):
    ''' Memory Item '''
    name = models.CharField(max_length=64)
    comment = models.TextField()
    longitude = models.CharField(max_length=64)
    latitude = models.CharField(max_length=64)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='memories')

    def __str__(self):
        ''' Magic method '''
        return self.name

    def get_absolute_url(self):
        ''' Get absolute url '''
        return reverse("memories:details", args=[self.pk])
