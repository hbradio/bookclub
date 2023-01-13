from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    pass

class Discussion(models.Model):
    book_title = models.CharField(max_length=100)
    meeting_date = models.DateField('meeting date')
    creator = models.ForeignKey(
      settings.AUTH_USER_MODEL,
      on_delete=models.CASCADE
    )

    def __str__(self):
        return self.book_title

class Thread(models.Model):
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)
    topic = models.CharField(max_length=255)
    created_datetime = models.DateTimeField('created date')
    creator = models.ForeignKey(
      settings.AUTH_USER_MODEL,
      on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.topic

class Post(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    content = models.TextField()
    created_datetime = models.DateTimeField('created date', null=True)
    author = models.ForeignKey(
      settings.AUTH_USER_MODEL,
      on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.author.username + '-' + self.created_datetime