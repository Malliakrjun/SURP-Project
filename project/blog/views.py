from .models import Post
from accounts.models import UserProfile
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
# from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
def post_list(request):
    object_list = Post.published.all()
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
    return render(request,'blog/post_list.html',{ 'page': page,'posts': posts})

    # posts = Post.published.all().order_by('published_date')
    # return render(request,'blog/post_list.html',{'posts': posts})


# def post_list(request):
#     posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     return render(request,'blog/post_list.html',{'posts':posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,status='published',publish__year=year,publish__month=month,publish__day=day)
    return render(request,'blog/post_detail.html',{'post': post,'user':request.user})

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