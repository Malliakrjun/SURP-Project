from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# import datetime
# Create your models here.
class event(models.Model):
    host = models.ForeignKey(User,related_name='creator',blank=True)
    event_title = models.CharField(max_length=200,default='')
    event_time = models.DateTimeField(null=True)
    interested_users=models.ManyToManyField(User,blank=True)
    description = models.TextField()
    venue = models.CharField(max_length=150)
    image = models.ImageField(upload_to='event_images',blank=True)
    # def is_incomplete(self):
    #     return self.event_time <= datetime.now()

    incomplete = models.BooleanField(default=False)

    def __str__(self):
        return self.event_title

class Event_Comment(models.Model):
    event = models.ForeignKey(event, related_name='comments')
    author=models.CharField(max_length=100,default='')
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)
    class Meta:
        ordering = ('created',)
    def __str__(self):
        return 'Comment by {} on {}'.format(self.author, self.post)