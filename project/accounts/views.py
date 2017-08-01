from django.shortcuts import render,redirect
from accounts.forms import (
    RegistrationForm,
    EditProfileForm,
)
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from accounts.models import UserProfile
from blog.models import Post
from blog.forms import PostForm
from events.models import event
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login
from django.template.defaultfilters import slugify

# Create your views here.
def home(request):
    x=request.user.is_superuser
    if not x:
        userpro=UserProfile.objects.get(user=request.user)
    else:
        userpro=User.objects.get(username='malli')
    return render(request,'accounts\home.html',{'userpro':userpro,})


def register(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account/login')
    else:
        form=RegistrationForm()
        args={'form':form}
        return render(request,'accounts/reg_form.html',args)

def post_profile(request):
    return view_profile(request)

@login_required
def view_profile(request):
    events=event.objects.all()
    object_list=Post.objects.filter(author=request.user)
    userpro=UserProfile.objects.get(user=request.user)
    events_attending=request.user.event_set.all()


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

    index = paginator.page_range.index(posts.number)
    max_index = len(paginator.page_range)
    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index
    page_range = paginator.page_range[start_index:end_index]

    if request.method == 'GET':
        form = PostForm()
    else:
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
        # Assign the current post to the comment
            new_post.author=request.user
            new_post.status='published'
            new_post.slug=slugify(new_post.title)
            new_post.post_image=request.FILES['post_image']
        # Save the comment to the database
            new_post.save()
            form=PostForm()
            return redirect('/account/profile/post/')
    args={'userpro':userpro,'events':events,'events_attending':events_attending,'posts':posts,'form':form,'page_range':page_range}
    return render(request,'accounts/profile.html',args)


@login_required
def edit_profile(request):
    if request.method=='POST':
        form=EditProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/account/profile')

    else:
        form=EditProfileForm(instance=request.user)
        args={'form':form}
        return render(request,'accounts/edit_profile.html',args)


@login_required
def change_password(request):
    if request.method=='POST':
        form =PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('/account/profile')
        else:
            return render('accounts/change-password.html')
    else:
        form=PasswordChangeForm(user=request.user)
        args={'form':form}
        return render(request,'accounts/change_password.html',args)

def myuser_login(request, *args, **kwargs):
    if request.user.is_authenticated():
        return redirect('/account/profile')

    return login(request, *args, **kwargs)