from django.db import models

# Create your models here.
class Todo(models.Model):
    task=models.CharField(max_length=100)
    description= models.TextField()
    completed= models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateField(auto_now=True)
    def __str__(self) -> str:
        return self.task