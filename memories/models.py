from django.db import models

class MemoryItem(models.Model):
    name = models.CharField(max_length=64)
    comment = models.TextField()

    def __str__(self):
        return self.name
