from django.db import models
from django.contrib.auth.models import User
class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user    = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
