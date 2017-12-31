from django import template
register = template.Library()
from ..models import Post
from django.db.models import Count
from accounts.models import UserProfile
from django.contrib.auth.models import User

@register.simple_tag
def total_posts():
    return Post.published.count()

@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-updated')[:count]
    return {'latest_posts': latest_posts}


@register.assignment_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]

@register.assignment_tag
def get_commenter(name):
    user=User.objects.get(username=name)
    userpro=user.userprofile
    return userpro.image.url
