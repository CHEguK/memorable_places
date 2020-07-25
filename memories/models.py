from django.db import models
from django.urls import reverse

class MemoryItem(models.Model):
    name = models.CharField(max_length=64)
    comment = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("memories:details", args=[self.pk])
