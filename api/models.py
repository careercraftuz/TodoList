from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=255, blank=True)
    status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
