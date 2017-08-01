from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils import timezone


# Create your models here.

class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager,self).get_queryset().filter(city='London')

class UserProfile(models.Model):
    user=models.OneToOneField(User)
    description=models.TextField(default='')
    locality=models.CharField(max_length=100,default='')
    city=models.CharField(max_length=100,default='')
    phone=models.IntegerField(default=0)
    image=models.ImageField(upload_to='profile_image',blank=True)
    back_image=models.ImageField(upload_to='back_image',blank=True)
    interests_choices = (
        ('All','All'),
        ('Malnutrition', 'Malnutrition'),
        ('Education', 'Education'),
        ('Poverty', 'Poverty'),
        ('Social Welfare', 'Social Welfare'),
        ('Hygiene and Sanitation', 'Hygiene and Sanitation'),
    )
    user_interests = models.CharField(
        max_length=25,
        choices=interests_choices,
        default='All'
    )
    # activation_key = models.CharField(max_length=40,default='')
    # key_expires = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username


def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile=UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile,sender=User)