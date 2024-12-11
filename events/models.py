from django.db import models

# Create your models here.
from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    notification = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    