from django.shortcuts import render,redirect
from accounts.forms import (
    RegistrationForm,
    EditProfileForm,

)
from accounts.models import UserProfile
from blog.models import Post
from events.models import event
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login
# Create your views here.
def home(request):
    return render(request,'accounts\home.html')


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

@login_required
def view_profile(request):
    x=request.user.is_superuser
    events=event.objects.all()
    posts=Post.objects.filter(author=request.user)
    if not x:
        userpro=UserProfile.objects.get(user=request.user)
    else:
        userpro=User.objects.get(username='malli')
    args={'userpro':userpro,'events':events,'posts':posts}
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