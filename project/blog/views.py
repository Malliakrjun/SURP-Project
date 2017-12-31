from .models import Post
from accounts.models import UserProfile
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
# from .forms import PostForm
from django.shortcuts import redirect
#from django.views.generic import RedirectView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth.models import User
from .forms import CommentForm

# Create your views here.
def post_list(request):
    if request.user.is_authenticated:
        userpro=UserProfile.objects.get(user=request.user)
    # else:
    #     userpro=None

    object_list = Post.published.all()
    if request.user.is_authenticated():
        latest_user_posts=object_list.filter(author=request.user)[:5]
    paginator = Paginator(object_list, 3) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
 # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
 # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    if request.user.is_authenticated():
        return render(request,'blog/post_list.html',{'posts': posts,'userpro':userpro,'latest_user_posts':latest_user_posts})
    else:
        return render(request,'blog/post_list.html',{'posts': posts,'latest_user_posts':''})

    # return render(request,'blog/post_list.html',{ 'page': page,'posts': posts})

    # posts = Post.published.all().order_by('published_date')
    # return render(request,'blog/post_list.html',{'posts': posts})


# def post_list(request):
#     posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     return render(request,'blog/post_list.html',{'posts':posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,status='published',created__year=year,created__month=month,created__day=day)
    # List of active comments for this post
    comments = post.comments.filter(active=True)
    if request.method == 'POST':
        # x=request.user.is_superuser
        # if not x:
        #     userpro=UserProfile.objects.get(user=request.user)
        # else:
        #     userpro=User.objects.get(username='malli')
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
        # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
        # Assign the current post to the comment
            new_comment.author=request.user
            new_comment.post = post
            new_comment.created = timezone.now()
        # Save the comment to the database
            new_comment.save()
            render(request,'blog/post_detail.html',{'post': post,'comments': comments,'comment_form': comment_form})
    else:
        comment_form = CommentForm()
    return render(request,'blog/post_detail.html',{'post': post,'comments': comments,'comment_form': comment_form})

# def post_detail(request,pk):
#     post=get_object_or_404(Post,pk=pk)
#     return render(request,'blog/post_detail.html',{'post':post,'user':request.user})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():                    #is_valid checks whether entered values are valid
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def doubt(request):
    return render(request,'blog/doubt.html')