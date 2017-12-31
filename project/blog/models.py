from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from accounts.models import UserProfile

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='created',null=True)
    author = models.ForeignKey(User,related_name='author')
    body = models.TextField()
    likes = models.ManyToManyField(User,blank=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True,null=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    post_image=models.ImageField(upload_to='blog_images',blank=True)
    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return self.title

    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    def get_absolute_url(self):
        return reverse('blog:post_detail',args=[self.created.year,self.created.strftime('%m'),self.created.strftime('%d'),self.slug])

# class Images(models.Model):
#     post = models.ForeignKey(Post, default=None)
#     image = models.ImageField(upload_to='blog_images',verbose_name='Image', )

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')
    author = models.ForeignKey(User,related_name='comments_by_author')
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)
    class Meta:
        ordering = ('created',)
    def __str__(self):
        return 'Comment by {} on {}'.format(self.author, self.post)