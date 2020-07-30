from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class MemoryItem(models.Model):
    name = models.CharField(max_length=64)
    comment = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='memories')

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse("memories:details", args=[self.pk])
