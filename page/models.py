from django.db import models
from django.utils import timezone
# Create your models here.

class Blog(models.Model):
    img = models.ImageField(default = 'blogs/default.jpg',upload_to = 'blogs')
    title = models.CharField(max_length = 100)
    date_posted = models.DateTimeField(default=timezone.now)
    link = models.TextField(default=None)

    def __str__(self) -> str:
        return self.title

class Project(models.Model):
    img = models.ImageField(default = 'projects/default.jpg',upload_to = 'projects')
    title = models.CharField(max_length = 100)
    date_posted = models.DateTimeField(default=timezone.now)
    link = models.TextField(default=None)

    def __str__(self) -> str:
        return self.title

class Presentation(models.Model):
    img = models.ImageField(default = 'presentations/default.jpg',upload_to = 'presentations')
    title = models.CharField(max_length = 100)
    date_posted = models.DateTimeField(default=timezone.now)
    link = models.TextField(default=None)

    def __str__(self) -> str:
        return self.title
